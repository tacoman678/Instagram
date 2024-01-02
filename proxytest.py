from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

chromedriver_path = r'C:\Users\16306\Desktop\Python Projects\Instagram\chromedriver-win64\chromedriver.exe'

options = ChromeOptions()

options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")
driver = Chrome(options=options)
driver.get('https://free-proxy-list.net/')

driver.get('http://httpbin.org/ip')
print(driver.find_element(By.TAG_NAME, "body").text)

# free proxy server URL
# proxy_server_url = "67.43.228.250"
# options.add_argument(f'--proxy-server={proxy_server_url}')
# driver = Chrome(options=options)
driver.get('http://httpbin.org/ip')
print(driver.find_element(By.TAG_NAME, "body").text)
driver.quit()

