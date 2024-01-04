from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
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
        self.url = 'https://www.instagram.com/'
        self.count = 0

    def login(self, cookies_path):
        random_user_agent = random.choice(self.user_agents)
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f"webdriver.chrome.driver={self.driver_path}")
        chrome_options.add_argument(f"--user-agent={random_user_agent}")
        self.driver = Chrome(options=chrome_options)

        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(random.uniform(0,5))
        #if it is your first time running this script comment out the next 4 lines, uncomment the next time once cookies.pkl is populated
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

    def find_followers(self, mentor_username, follow_limit):
        self.driver.get(url=f"{self.url}{mentor_username}")
        sleep(random.uniform(0,5))

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')))
        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(random.uniform(0,5))

        WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div')))
        modal = self.driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div')
        self.buttons = modal.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30')
        self.names = modal.find_elements(By.CSS_SELECTOR, 'span._ap3a._aaco._aacw._aacx._aad7._aade')
        sleep(random.uniform(0,5))
        self.follow(follow_limit)

    def follow(self, follow_limit):
        for button, name in zip(self.buttons, self.names):
            if(self.count == follow_limit):
                with open('cookies.pkl', 'wb') as cookies_file:
                    pickle.dump(self.driver.get_cookies(), cookies_file)
                self.driver.quit()
                return
            sleep(random.uniform(9,11))
            button.click()
            print("followed:",name.text)
            self.count += 1
        random_user = random.choice(self.names)
        self.find_followers(random_user, follow_limit)

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

#create a credentials.txt in the same folder as this file, format "YOUR_USERNAME:YOUR_PASSWORD"
credentials = read_credentials("credentials.txt")
#replace with the path to chromedriver that corresponds with your version of chrome
chromedriver_path = r'C:\Users\16306\Desktop\Python Projects\Instagram\chromedriver-win64\chromedriver.exe'
bot = Instabot(username=credentials[0]['username'], password=credentials[0]['password'], driver_path=chromedriver_path)
bot.login(cookies_path="cookies.pkl")
#replace with your targeted insta account username
bot.find_followers(mentor_username="leomessi", follow_limit=60)