import time
import os
import random
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

EMAIL = os.environ.get("INSTA_EMAIL")
USERNAME = os.environ.get("INSTA_USER")
PASSWORD = os.environ.get("INSTA_PASS")
INSTAGRAM_URL = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(INSTAGRAM_URL)

    def login(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(USERNAME)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div").click()
        self.delay()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
        self.delay()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    def delay(self):
        self.wait_time = random.uniform(4, 10)
        time.sleep(self.wait_time)

    def find_followers(self):
        self.delay()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div").click()
        self.delay()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(10)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "mad_about_food").click()
        self.delay()
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").click()
        self.delay()
        time.sleep(8)

    def follow(self):
        for num in range(1, 11):
            xpath = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{num}]/div/div/div/div[3]/div/button"
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                element.click()
                self.delay()
                print("Followed:", num)
            except NoSuchElementException as e:
                print(f"Error following element {num}: {e}")


insta_bot = InstaFollower()
insta_bot.login()
time.sleep(15)
insta_bot.find_followers()
time.sleep(14)
insta_bot.follow()
print("Well done, Congrats!")