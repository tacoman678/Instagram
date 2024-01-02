from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep, strftime
from random import randint
import pandas as pd
import pickle

class Instabot:
    def __init__(self, username, password, driver_path):
        self.user = username
        self.passw = password
        self.driver_path = driver_path

    def login(self):
        chrome_options = Options()
        chrome_options.add_argument(f"webdriver.chrome.driver={self.driver_path}")
        webdriver = webdriver.Chrome(options=chrome_options)
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(1)
        username_input = webdriver.find_element(By.NAME, 'username')
        username_input.send_keys(self.username) 
        sleep(1)
        password_input = webdriver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        sleep(1)
        button_login = webdriver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        button_login.click()
        return webdriver
    
    def login(self, delay_low, delay_high, headless_mode):
        chrome_options = Options()
        chrome_options.add_argument(f"webdriver.chrome.driver={self.driver_path}")
        webdriver = webdriver.Chrome(options=chrome_options)
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        return webdriver
    
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
