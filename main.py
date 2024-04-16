import os
import time
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager
from selenium.webdriver.chrome.service import Service as ChromeService




if __name__ == '__main__':
    dotenv_path = find_dotenv()  # finds the .env file path
    load_dotenv(dotenv_path)  # loads the .env file from the path found above

    ZIPCODE_URL: str = os.getenv("ZIPCODE")

    chrome_driver_path = ChromeDriverManager().install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(name="detach", value=True)
    # Keep the browser open when the script finishes - unless you use driver.quit()

    service = ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(ZIPCODE_URL)

