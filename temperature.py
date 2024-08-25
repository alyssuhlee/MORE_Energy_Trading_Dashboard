# Necessary imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import schedule
import time

def get_temp_and_weather():
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
    # Find the weather condition element in the page
    weather_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/div[1]")
    # Extract the temperature value
    temperature = temp_element.text if temp_element else 'Not found'
    # Extract the weather condition value
    weather = weather_element.text if weather_element else 'Not found'

    # Close the WebDriver
    driver.quit()

    # Create a DataFrame with the scraped temperature value
    df = pd.DataFrame({'Temperature': [temperature]})
    # Get the current date and time
    now = datetime.now()
    # Get current date
    date_today = now.strftime("%m/%d/%Y")
    # Get current hour
    current_hour = now.strftime("%H")
    # Insert Weather Condition in the 2nd column
    df.insert(1, "Weather Condition", weather)
    # Insert Date Today in the 3rd column
    df.insert(2, "Date Today", date_today)
    # Insert Current Hour in the 4th column
    df.insert(3, "Current Hour", current_hour)

    # Transfer data to an Excel file
    df.to_excel('temp_data.xlsx', index=False)

# Schedule the task to run every hour
schedule.every().hour.do(get_temp_and_weather)

# Run the scheduler
print("Scheduler started. Fetching data every hour...")
while True:
    schedule.run_pending()
    time.sleep(1)