# Necessary imports
from datetime import datetime
import mysql.connector
import time

# MySQL connection details
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'myDb'
}

# Function to determine the time interval
def get_time_interval(current_time):
    # Get the current hour
    hour = current_time.hour
    # Get the current minute
    minute = current_time.minute
    
    # If the time is exactly 12:00 AM
    if hour == 0 and minute == 0:
        return '2400 H'
    # If the time is between 12:01 AM and 12:59 AM
    elif hour == 0:
        return '0100 H'
    elif hour == 23 and minute > 0:
        return '2400 H'
    # If the time is exactly on the hour (e.g., 1:00 AM, 2:00 AM)
    elif minute == 0:
        return f'{hour:02}00 H'
    # For all other times, return the next hour followed by "00 H"
    else:
        return f'{(hour + 1) % 24:02}00 H'

# Function to insert the time interval into the database
def insert_time_interval(time_interval):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS TimeIntervals (
            id INT AUTO_INCREMENT PRIMARY KEY,
            time_interval VARCHAR(10) NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Insert the time interval
        cursor.execute("INSERT INTO TimeIntervals (time_interval) VALUES (%s)", (time_interval,))
        
        # Commit the transaction
        conn.commit()
        
        print("Time interval inserted:", time_interval)
        
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

# Main loop to update the database every minute
while True:
    # Get the current time
    now = datetime.now()
    
    # Determine the time interval
    time_interval = get_time_interval(now)
    
    # Insert the time interval into the database
    insert_time_interval(time_interval)
    
    # Wait for 800 seconds before checking again
    time.sleep(800)