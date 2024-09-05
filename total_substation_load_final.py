# Necessary imports
from mysql.connector import Error
from openpyxl import load_workbook
from sqlalchemy import create_engine
import datetime
import mysql.connector
import pandas as pd
import threading
import time

# File locations
file_loc = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\\'
current_day = datetime.datetime.today()

def query_substation_data():
    try:
        # Create SQLAlchemy engine
        engine = create_engine('mysql+mysqlconnector://mepcadmi_guest:hJER8pBv8WyS@192.185.52.175/mepcadmi_empower')

        query = (
            "SELECT substation, feeder_no, date_entered, time_entered, load_kw, meter_reading, main_meter "
            "FROM mepcadmi_empower.substation_load WHERE date_entered = '{}' "
        ).format(current_day.strftime('%Y-%m-%d'))

        substation_load_df = pd.read_sql(query, engine, parse_dates={"date_entered": {"format": "%d/%m/%y"}})
        substation_load_df = substation_load_df.sort_values(by=['date_entered', 'time_entered'])

        substation_load_df = pd.pivot_table(substation_load_df, values='load_kw',
                                            index=['date_entered', 'time_entered'], columns='substation',
                                            aggfunc='sum')
        substation_load_df['10 MVA Mobile SS - MS1'] = 0
        substation_load_df['MOLO SUBSTATION'] = 0
        substation_load_df = substation_load_df[
            ['LAPAZ SUBSTATION', 'JARO SUBSTATION', 'MANDURRIAO SUBSTATION', 'MOLO SUBSTATION',
             'DIVERSION SUBSTATION', '10 MVA Mobile SS - MS1', '36 MVA Mobile SS - MS2', '36 MVA Megaworld SS - MGW']]
        substation_load_df = substation_load_df.reset_index()
        substation_load_df.columns = ['Date', 'Hour', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
        substation_load_df.fillna(0, inplace=True)
        substation_load_df['Total'] = substation_load_df['S1'] + substation_load_df['S2'] + substation_load_df['S3'] + \
                                      substation_load_df['S4'] + substation_load_df['S5'] + substation_load_df['S6'] + \
                                      substation_load_df['S7'] + substation_load_df['S8']
        substation_load_df['eS1'] = substation_load_df['S1'] * 1.0001
        substation_load_df['eS2'] = substation_load_df['S2'] * 1.0001
        substation_load_df['eS3'] = substation_load_df['S3'] * 1.0001
        substation_load_df['eS4'] = substation_load_df['S4'] * 1.0001
        substation_load_df['eS5'] = substation_load_df['S5'] * 1.0001
        substation_load_df['eS6'] = substation_load_df['S6'] * 1.0001
        substation_load_df['eS7'] = substation_load_df['S7'] * 1.0001
        substation_load_df['eS8'] = substation_load_df['S8'] * 1.0001
        substation_load_df = substation_load_df[substation_load_df['Hour'] != 0]
        substation_load_df = substation_load_df.fillna(0)
        substation_load_df['eTotal'] = substation_load_df['eS1'] + substation_load_df['eS2'] + substation_load_df[
            'eS3'] + substation_load_df['eS4'] + substation_load_df['eS5'] + substation_load_df['eS6'] + \
                                       substation_load_df['eS7'] + substation_load_df['eS8']

        substation_load_df.to_csv(file_loc + 'station_load.csv', index=False)
        print("Substation data queried and saved to CSV.")

    except Exception as e:
        print(e)

def get_current_hour():
    now = datetime.datetime.now()
    current_hour = now.hour
    if current_hour == 0:
        return 24
    return current_hour

def get_total_for_current_hour(excel_file, current_hour):
    try:
        df = pd.read_excel(excel_file, header=None, names=['Date', 'Hour', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Total', 'eS1', 'eS2', 'eS3', 'eS4', 'eS5', 'eS6', 'eS7', 'eS8', 'eTotal'], skiprows=1)
        
        if df.empty:
            print("Excel file is empty.")
            return None

        if current_hour not in df['Hour'].values:
            print(f"No data for the current hour: {current_hour}")
            return None

        total_substation_load_value = df.loc[df['Hour'] == current_hour, 'Total'].values[0]
        return float(total_substation_load_value) if pd.notnull(total_substation_load_value) else None
    except Exception as e:
        print(f"Error retrieving total substation load value from Excel: {e}")
        return None

def insert_into_mysql(conn, total_substation_load_value):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO total_substation_load (substation_load) VALUES (%s)"
        cursor.execute(sql, (total_substation_load_value,))
        conn.commit()
        cursor.close()
        print(f"Value {total_substation_load_value} inserted successfully into MySQL.")
    except mysql.connector.Error as e:
        print(f"Error inserting into MySQL: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main(excel_file, conn):
    while True:
        try:
            current_hour = get_current_hour()
            total_substation_load_value = get_total_for_current_hour(excel_file, current_hour)
            if total_substation_load_value is not None:
                insert_into_mysql(conn, total_substation_load_value)
            else:
                print(f"Invalid total_substation_load_value: {total_substation_load_value}")
            time.sleep(800)
        except KeyboardInterrupt:
            print("\nTerminating the script.")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(60)

def query_run():
    while True:
        query_substation_data()
        read_file = pd.read_csv(file_loc + 'station_load.csv')
        read_file.to_excel(file_loc + 'station_load.xlsx', index=False, header=True)
        print("station_load.xlsx updated from station_load.csv.")
        time.sleep(800)

if __name__ == "__main__":
    query_thread = threading.Thread(target=query_run, daemon=True)
    query_thread.start()

    excel_file = file_loc + 'station_load.xlsx'

    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='myDb',
            user='root',
            password=''
        )

        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS total_substation_load (
                id INT AUTO_INCREMENT PRIMARY KEY,
                substation_load FLOAT(10, 2) NOT NULL,
                insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.close()

        main(excel_file, conn)

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")