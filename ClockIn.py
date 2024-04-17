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

        self.clock_in()

    def clock_in(self):
        self.driver.get(self.URL)  # Go to the zipcode home page

        self.login()

    def login(self) -> None:
        time.sleep(2)  # Sleep for two seconds
        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="block-bartik-account-menu"]/div/ul/li/a')
        login_button.click()

        self.enter_username_password()

        login_button = self.driver.find_element(by=By.ID, value="edit-submit")
        time.sleep(1)
        login_button.click()

        self.go_to_home_page()

        time.sleep(1)
        self.get_login_button()

    def enter_username_password(self) -> None:
        # Enter UN
        username_field = self.driver.find_element(by=By.ID, value="edit-name")
        username = os.getenv("USERNAME")
        username_field.send_keys(username)

        # Enter PW
        password_field = self.driver.find_element(by=By.ID, value="edit-pass")
        pwd = os.getenv("PASSWORD")
        password_field.send_keys(pwd)

    def go_to_home_page(self):
        home_button = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="block-bartik-breadcrumbs"]/div/nav/ol/li/a')
        home_button.click()

    def get_login_button(self):
        login_button = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="block-bartik-content"]'
                                                      '/div[1]/div[1]/div/div/form/input[4]')
        login_button.click()
