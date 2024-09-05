# Necessary imports
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import Options for headless mode
import os
import pandas as pd
import time

def fetch_weather_data():
    # # Set up Selenium options
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)

    # # Initialize the webdriver
    # driver = webdriver.Chrome()

    # Set up options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
    chrome_options.add_argument("--window-size=1920,1080")  # Set the window size (optional)

    # Initialize the WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    # URL of The Weather Channel
    url = 'https://weather.com/en-TT/weather/today/l/d5c2f0e4c2053e855f8c6f30f8c21aedcedfe8c9f8842071a894732e8b0eff99'
    driver.get(url)

    # Find the temperature element in the page
    temp_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/span")
    # Find the weather condition element in the page
    weather_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/div[1]")
    # Extract the temperature value
    temperature = temp_element.text.replace("°", "") if temp_element else "Not found"
    # Extract the weather condition 
    weather = weather_element.text if weather_element else 'Not found'

    # Close the webdriver
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

if __name__ == "__main__":
    while True:
        fetch_weather_data()
        time.sleep(600) # Every 600 seconds