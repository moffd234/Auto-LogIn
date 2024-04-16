import os
import time
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager
from selenium.webdriver.chrome.service import Service as ChromeService

dotenv_path = find_dotenv()  # finds the .env file path
load_dotenv(dotenv_path)  # loads the .env file from the path found above

class ClockIn:
    def __init__(self):
        self.URL: str = os.getenv("ZIPCODE")
        chrome_driver_path = ChromeDriverManager().install()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)

        service = ChromeService(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.clockIn()

    def clockIn(self):
        self.driver.get(self.URL)  # Go to the zipcode home page

        self.logIn()

    def logIn(self):
        time.sleep(2)  # Sleep for two seconds
        
