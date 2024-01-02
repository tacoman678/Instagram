from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd 

chromedriver_path = r'C:\Users\16306\Desktop\Python Projects\Instagram\chromedriver-win64\chromedriver.exe'

options = ChromeOptions()

options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")
driver = Chrome(options=options)
driver.get('https://free-proxy-list.net/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_div = soup.find('div', class_='table-responsive')
rows = table_div.find('tbody').find_all('tr')

data = []

for row in rows:
    ip_address = row.find('td').text
    port_number = row.find_all('td')[1].text
    orgin = row.find('td', class_='hm').text.strip()
    https_support = row.find('td', class_='hx').text.strip()
    data.append({'IP Address': ip_address, 'Port Number':port_number, 'Orgin':orgin, 'Https Support': https_support})

df = pd.DataFrame(data)
filtered_df = df[(df['Https Support'] == 'yes') & (df['Orgin'] == 'United States')]
print(filtered_df)
sleep(1)

driver.get('http://httpbin.org/ip')
print(driver.find_element(By.TAG_NAME, "body").text)

if not filtered_df.empty:
    proxy_server_url = filtered_df.iloc[0]['IP Address'] + ':' + filtered_df.iloc[0]['Port Number']
    options2 = ChromeOptions()
    options2.add_argument(f"webdriver.chrome.driver={chromedriver_path}")
    options2.add_argument(f'--proxy-server={proxy_server_url}')
    driver = Chrome(options=options2)
    driver.get('http://httpbin.org/ip')
    print(driver.find_element(By.TAG_NAME, "body").text)
    driver.quit()
else:
    print("No proxies available with HTTPS support in the US.")
driver.quit()