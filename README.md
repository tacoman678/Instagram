# Instagram Automation Tools

This repository contains Python scripts for automating tasks related to Instagram, utilizing the Selenium WebDriver and undetected_chromedriver library.

## Instabot.py

The `Instabot.py` script is designed to automate Instagram interactions, such as logging in, following users, and gathering follower information.

### Features:

- Login to Instagram using specified credentials.
- Follow a specified number of followers of a given Instagram account.
- Utilize undetected_chromedriver and rotating user agents to prevent detection.
        - __Use of a VPN or Proxies is recommended; see proxyTest.py for implementation.__

### Usage:

1. Ensure you have the required dependencies installed: undetected_chromedriver, Selenium, pandas, and pickle.
        -pip install undetected_chromedriver, Selenium, pandas, and pickle
2. Create a `credentials.txt` file in the same folder with the format "YOUR_USERNAME:YOUR_PASSWORD".
3. Replace the `chromedriver_path` variable with the path to your ChromeDriver executable.
4. Instantiate the `Instabot` class with your credentials and driver path.
5. Run once to gather cookies.
6. Run the `find_followers` method with the target Instagram account and follow limit.

## proxyTest.py

The `proxyTest.py` script demonstrates how to scrape and test free proxy servers for use with web scraping tasks.

### Features:

- Scrape a list of free proxy servers.
- Test the proxies for HTTPS support and geographical origin.
- Utilize a working proxy to access a test website.

### Usage:

1. Replace the `chromedriver_path` variable with the path to your ChromeDriver executable.
2. Run the script to scrape and test free proxy servers.

## userAgentTest.py

The `userAgentTest.py` script showcases how to set and rotate user agents while web scraping.

### Features:

- Scrape the current user agent from a website.
- Rotate through a list of predefined user agents for anonymity.
- Utilize headless mode for silent browsing.

### Usage:

1. Replace the `chromedriver_path` variable with the path to your ChromeDriver executable.
2. Run the script to observe user agent changes.

Feel free to explore and customize these scripts based on your specific needs. If you encounter any issues, check the dependencies and ensure your environment is set up correctly.
