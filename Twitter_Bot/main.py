from os import getenv
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv(dotenv_path=find_dotenv())


# Environment Variables => Twitter
TWITTER_EMAIL = getenv("TWITTER_EMAIL")
TWITTER_USERNAME = getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = getenv("TWITTER_PASSWORD")

# Setting up Selenium:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

upload_speed = 0
download_speed = 0


class TwitterNetBot:

    def get_internet_speed():
        """This will get the internet speed"""

        driver.get(url="https://www.speedtest.net/")
        time.sleep(60)

        go_button = driver.find_element(
            by=By.XPATH,
            value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]",
        )
        go_button.click()
        print("GOT CLICKED")

        time.sleep(60)

        global upload_speed, download_speed

        upload_speed = driver.find_element(
            by=By.XPATH,
            value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span",
        ).text
        download_speed = driver.find_element(
            by=By.XPATH,
            value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span",
        ).text

        print(download_speed)
        print(upload_speed)

    def twitter_login():
        """This would login to one's twitter account"""

        driver.get(url="https://twitter.com/i/flow/login")

        time.sleep(20)

        email_login = driver.find_element(
            by=By.XPATH,
            value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input",
        )
        email_login.send_keys(TWITTER_EMAIL)
        email_login.send_keys(Keys.ENTER)

        time.sleep(10)

        username_login = driver.find_element(
            by=By.XPATH,
            value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
        )
        username_login.send_keys(TWITTER_USERNAME)
        username_login.send_keys(Keys.ENTER)

        time.sleep(10)

        password_login = driver.find_element(
            by=By.XPATH,
            value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        )
        password_login.send_keys(TWITTER_PASSWORD)
        password_login.send_keys(Keys.ENTER)


bot = TwitterNetBot
# bot.get_internet_speed()
bot.twitter_login()
