from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
]

chromedriver_path = r'C:\Users\16306\Desktop\Python Projects\Instagram\chromedriver-win64\chromedriver.exe'

options = ChromeOptions()

options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")
driver = Chrome(options=options)
driver.get('https://useragentstring.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
user_agent = soup.find('textarea').text
driver.quit()
print(user_agent)
random_user_agent = random.choice(user_agents)
options2 = ChromeOptions()
options2.add_argument(f"webdriver.chrome.driver={chromedriver_path}")
options2.add_argument(f"--user-agent={random_user_agent}")
options2.add_argument("--headless")
driver = Chrome(options=options2)
driver.get('https://useragentstring.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
user_agent = soup.find('textarea').text
print(user_agent)
driver.quit()