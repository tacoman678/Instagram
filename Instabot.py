from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
import pandas as pd
import pickle

class Instabot:
    def __init__(self, username, password, driver_path):
        self.username = username
        self.password = password
        self.driver_path = driver_path
        self.user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"]

    def login(self, cookies_path):
        random_user_agent = random.choice(self.user_agents)
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f"webdriver.chrome.driver={self.driver_path}")
        chrome_options.add_argument(f"--user-agent={random_user_agent}")
        self.driver = Chrome(options=chrome_options)

        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(random.uniform(0,5))
        with open(cookies_path, 'rb') as cookies_file:
            cookies = pickle.load(cookies_file)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(self.username) 
        sleep(random.uniform(0,5))

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        sleep(random.uniform(0,5))

        button_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        button_login.click()
        sleep(random.uniform(0,5))

    def read_credentials(file_path):
        credentials = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    username, password = line.strip().split(':')
                    credentials.append({'username': username, 'password': password})
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading credentials: {e}")
        return credentials
