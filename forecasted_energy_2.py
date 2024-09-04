
# File paths for source and destination Excel files
source_file_path = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\cloned_file.xlsx'
destination_file_path = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\forecasted_energy.xlsx'

# Load source workbook
source_wb = load_workbook(source_file_path, data_only=True)  # Use data_only=True to get values instead of formulas
source_sheet = source_wb['6. DAP Report']

# Load destination workbook
dest_wb = load_workbook(destination_file_path)
dest_sheet = dest_wb['Sheet']

# Define source and destination ranges
source_ranges = [('C11', 'C34'), ('F11', 'F34')]
dest_ranges = [('A2', 'A25'), ('B2', 'B25')]

# Function to copy values from source range to destination range
def copy_values(source_sheet, dest_sheet, source_range, dest_range):
    source_start, source_end = source_range
    dest_start, dest_end = dest_range
    
    # Copy values from source to destination
    source_values = []
    for row in source_sheet[source_start:source_end]:
        for cell in row:
            source_values.append(cell.value)
    
    dest_index = 0
    for row in dest_sheet[dest_start:dest_end]:
        for cell in row:
            if dest_index < len(source_values):
                cell.value = source_values[dest_index]
                dest_index += 1
            else:
                break

# Copy data from source to destination based on specified ranges
for i in range(len(source_ranges)):
    copy_values(source_sheet, dest_sheet, source_ranges[i], dest_ranges[i])

# Save the destination workbook
dest_wb.save(destination_file_path)

# Close workbooks
source_wb.close()
dest_wb.close()

print("Data transfer completed.")

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
            CREATE TABLE IF NOT EXISTS your_table_name (
                id INT AUTO_INCREMENT PRIMARY KEY,
                hour_value DECIMAL(10, 2) NOT NULL,
                insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("MySQL table created successfully.")
    except 