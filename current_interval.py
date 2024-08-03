import mysql.connector
from datetime import datetime
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
    hour = current_time.hour
    if hour == 0:
        return '0100 H'
    elif hour == 23:
        return '2400 H'
    else:
        return f'{hour+1:02}00 H'

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
    
    # Wait for 300 seconds before checking again
    time.sleep(300)