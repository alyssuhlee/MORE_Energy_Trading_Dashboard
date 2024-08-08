# Necessary imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import glob
import os
import pandas as pd
import time

# Check expected columns based on header
def inspect_csv(file_path, encoding='utf-16', delimiter='\t'):
    with open(file_path, 'r', encoding=encoding) as infile:
        reader = csv.reader(infile, delimiter=delimiter)
        header = next(reader)
        
        # Clean the header by removing empty strings and stripping whitespace
        header = [col.strip() for col in header if col.strip()]
        expected_columns = len(header)
        
        print(f"Cleaned Header: {header}")
        print(f"Expected columns based on header: {expected_columns}")
        
        return expected_columns, header

def clean_csv(file_path, cleaned_file_path, encoding='utf-16', delimiter='\t', expected_columns=None):
    with open(file_path, 'r', encoding=encoding) as infile:
        reader = csv.reader(infile, delimiter=delimiter)
        data = list(reader)
        
        if expected_columns is None:
            expected_columns = len(data[0])
        
        cleaned_data = []
        for i, row in enumerate(data):
            if len(row) > expected_columns:
                # Adjust the row to have the expected number of columns
                new_row = row[:expected_columns-1] + [' '.join(row[expected_columns-1:])]
                cleaned_data.append(new_row)
            elif len(row) < expected_columns:
                # Handle rows with fewer columns (e.g., append empty strings)
                new_row = row + [''] * (expected_columns - len(row))
                cleaned_data.append(new_row)
            else:
                cleaned_data.append(row)
    
    # Write cleaned data to a new file
    with open(cleaned_file_path, 'w', encoding=encoding, newline='') as outfile:
        writer = csv.writer(outfile, delimiter=delimiter)
        writer.writerow(header)  # Write the cleaned header first
        writer.writerows(cleaned_data[1:])  # Write the data rows

# Function to remove specific problematic characters
def remove_problematic_characters(text):
    # Replace the problematic character \x02 (hex) or  (unicode) with an empty string
    return text.replace('\x02', '').replace('', '')

def main():
    driver = webdriver.Chrome()
    # URL of website
    url = 'https://embi.iemop.ph/t/tod/views/SYSTEM_ADVISORY/MARKETSYSTEMS?%3AshowAppBanner=false&%3Adisplay_count=n&%3AshowVizHome=n&%3Aorigin=viz_share_link&%3AisGuestRedirectFromVizportal=y&%3Aembed=y'
    # Opening the website
    driver.get(url) 
    # Maximize window
    driver.maximize_window()
    time.sleep(10)
    # Click 'Download'
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]").click()
    time.sleep(10)
    # Click 'Crosstab'
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div/button[3]").click()
    time.sleep(10)
    # Click 'Download'
    driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div[2]/div/div[2]/button").click()
    time.sleep(20)
    list_of_files = glob.glob(r'C:\Users\aslee\Downloads\*')
    # Finds the most recently created file from a list of files
    csv_file_path = max(list_of_files, key=os.path.getctime)
    final_csv_file_path = r'C:\Users\aslee\Downloads\ADV_crosstab.csv'

    for i in range(1, 100000):
        if csv_file_path == rf'C:\Users\aslee\Downloads\ADV_crosstab ({i}).csv':
            os.replace(csv_file_path, final_csv_file_path)
            break
    time.sleep(20)
    global header
    # Usage
    expected_columns, header = inspect_csv(final_csv_file_path, delimiter='\t')
    time.sleep(20)
    # Usage
    cleaned_csv_file_path = r'C:\Users\aslee\Downloads\cleaned_mo_advisories_file.csv'
    clean_csv(final_csv_file_path, cleaned_csv_file_path, encoding='utf-16', delimiter='\t', expected_columns=expected_columns)
    time.sleep(10)
    # Read the cleaned CSV file
    df = pd.read_csv(cleaned_csv_file_path, encoding='utf-16', delimiter='\t')
    time.sleep(10)
    # Clean each cell in the DataFrame
    df_cleaned = df.applymap(remove_problematic_characters)
    time.sleep(10)
    # Write the cleaned DataFrame to an Excel file
    excel_file_path = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\MO_ADVISORIES.xlsx'
    df_cleaned.to_excel(excel_file_path, index=False)
    print(f'CSV file "{cleaned_csv_file_path}" successfully converted to Excel file "{excel_file_path}"')

while True:
    main()
    time.sleep(3600) # Every 3600 seconds (1 hour)