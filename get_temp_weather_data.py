# Necessary Imports
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd
import time

def fetch_weather_data():
    # Set up Selenium options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)

    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # URL of the weather page
    url = 'https://weather.com/en-TT/weather/today/l/d5c2f0e4c2053e855f8c6f30f8c21aedcedfe8c9f8842071a894732e8b0eff99'
    driver.get(url)

    # Find the temperature element in the page
    temp_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/span")
    weather_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/div[1]")
    # Extract the temperature value
    temperature = temp_element.text.replace("°", "") if temp_element else "Not found"
    weather = weather_element.text if weather_element else 'Not found'

    # Close the WebDriver
    driver.quit()

    now = datetime.now()
    date_today = now.strftime("%m/%d/%Y")
    current_hour = now.strftime("%H")

    new_data = {
        "Temperature (in Celsius)": [temperature],
        "Weather Condition": [weather],
        "Date Today": [date_today],
        "Current Hour": [current_hour]
    }

    new_df = pd.DataFrame(new_data)

    # Filepath to the Excel file
    file_path = 'temp_data.xlsx'

    # Check if the Excel file exists
    if os.path.exists(file_path):
        # Read the existing data
        existing_df = pd.read_excel(file_path)
        # Append the new data
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        # If the file does not exist, use the new data as the DataFrame
        updated_df = new_df

    # Write the updated DataFrame back to the Excel file
    updated_df.to_excel(file_path, index=False)

while True:
    fetch_weather_data()
    time.sleep(3600)