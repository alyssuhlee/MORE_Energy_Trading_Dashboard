# Necessary imports
from datetime import datetime
import mysql.connector
import pandas as pd
import time

# Function to retrieve the current date
def get_current_date():
    now = datetime.now()
    current_date = now.strftime("%m/%d/%Y")
    return current_date

# Function to retrieve the current hour 
def get_current_hour():
    now = datetime.now()
    current_hour = now.hour
    if current_hour == 0:
        return 24
    return current_hour

# Function to retrieve temperature and weather condition from Excel for the current date and hour
def get_temp_weather_for_current_hour(excel_file, current_date, current_hour):
    try:
        # Read Excel file into a Pandas DataFrame
        df = pd.read_excel(excel_file, header=None, names=['Temperature', 'Weather Condition', 'Date Today', 'Current Hour'], skiprows=1)

        # Filter the row based on date and hour
        filtered_data = df[(df['Date Today'] == current_date) & (df['Current Hour'] == current_hour)]

        if not filtered_data.empty:
            temperature = filtered_data['Temperature'].values[0]
            weather_condition = filtered_data['Weather Condition'].values[0]
            return int(temperature), weather_condition
        else:
            return None, None
    except Exception as e:
        print(f"Error retrieving temperature and weather condition from Excel: {e}")
        return None, None

# Function to insert temperature and weather condition into MySQL
def insert_data_into_mysql(conn, temperature, weather_condition):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO temp_data (temp, weather) VALUES (%s, %s)"
        cursor.execute(sql, (temperature, weather_condition))
        conn.commit() # Commit the transaction
        cursor.close()
        print(f"Temperature {temperature} and Weather Condition {weather_condition} inserted successfully into MySQL.")
    except mysql.connector.Error as e:
        print(f"Error inserting temperature and weather condition into MySQL: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Main function to run the script
def main(excel_file, conn):
    current_date = get_current_date()
    while True:
        try:
            current_hour = get_current_hour()
            temperature, weather_condition = get_temp_weather_for_current_hour(excel_file, current_date, current_hour)

            if temperature is not None and weather_condition is not None:
                insert_data_into_mysql(conn, temperature, weather_condition)
            else:
                print(f"Invalid temperature valu: {temperature} and invalid weather condition value: {weather_condition}")
                
            time.sleep(800)
        
        except KeyboardInterrupt:
            print("\nTerminating the script.")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(60)  # Delay before retrying

if __name__ == "__main__":
    while True:
        excel_file = 'temp_data.xlsx'

        conn = mysql.connector.connect(
            host='localhost',
            database='myDb',
            user='root',
            password=''
        )
    
        # Create MySQL table if it doesn't exist
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS temp_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                temp INT,
                weather TEXT,
                insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.close()

        # Run main function to continuously check and update database
        main(excel_file, conn)