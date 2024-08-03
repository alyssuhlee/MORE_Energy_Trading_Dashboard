# For transferring the Forecasted Energy in the MySQL database
import pandas as pd
import mysql.connector
from datetime import datetime
import time

# Function to get current hour
def get_current_hour():
    now = datetime.now()
    current_hour = now.hour
    return current_hour

# Function to read Excel and get value for current hour
def get_value_for_current_hour(df, current_hour):
    try:
        net_value = df.loc[df['HOUR'] == current_hour, 'NET'].values[0]
        return net_value
    except IndexError:
        print(f"No value found for hour {current_hour}.")
        return None

# Function to create MySQL table if it doesn't exist
def create_mysql_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS forecasted_energy (
                id INT AUTO_INCREMENT PRIMARY KEY,
                net DECIMAL(10, 2) NOT NULL,
                insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("MySQL table created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating MySQL table: {e}")

# Function to insert value into MySQL database
def insert_into_mysql(cursor, value):
    try:
        sql = "INSERT INTO forecasted_energy (net) VALUES (%s)"
        cursor.execute(sql, (value,))
        print(f"Value {value} inserted successfully into MySQL.")
    except mysql.connector.Error as e:
        print(f"Error inserting into MySQL: {e}")

# Main function to run the script
def main(excel_file, cursor):
    # Load Excel data
    df = pd.read_excel(excel_file)

    while True:
        current_hour = get_current_hour()
        net_value = get_value_for_current_hour(df, current_hour)

        if net_value is not None and pd.notnull(net_value):
            # Convert net value to float to ensure compatibility with MySQL DECIMAL(10, 2)
            net_value = float(net_value)
            insert_into_mysql(cursor, net_value)
        else:
            print(f"Invalid net_value: {net_value}")
        
        # Delay for 1 hour (3600 seconds) before checking again
        time.sleep(3600)

if __name__ == "__main__":
    excel_file = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\forecasted_energy.xlsx'

    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            database = 'myDb',
            user = 'root',
            password = ''
        )
        cursor = conn.cursor()

        # Create MySQL table if it doesn't exist
        create_mysql_table(cursor)

        # Run main function to continuously check and update database
        main(excel_file, cursor)
    
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        cursor.close()
        conn.close()

'''
# -- CLONING AN EXCEL FILE TO A DIFFERENT PATH --
destination_path = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL' # Destination path where cloned file will be saved
wb = load_workbook(filename=folder_path_2) #Load the workbook
cloned_wb = Workbook() #Create a new workbook (clone)
for sheet_name in wb.sheetnames:
    original_sheet = wb[sheet_name]
    cloned_sheet = cloned_wb.create_sheet(title=sheet_name)
    for row in original_sheet.iter_rows(values_only=True):
        cloned_sheet.append(row)
cloned_filename = f"{destination_path}/cloned_file.xlsx"
cloned_wb.save(cloned_filename)
print(f"Excel file cloned and saved to: {cloned_filename}")
'''