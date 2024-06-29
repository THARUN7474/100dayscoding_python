from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = Chrome(self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        print()
        go_button = self.driver.find_element(By.CLASS_NAME, value='start-text')
        go_button.click()
        time.sleep(40)
        self.down = float(self.driver.find_element(By.CLASS_NAME, value='download-speed').text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value='upload-speed').text)
        # self.driver.quit()

    def tweet_at_provider(self, user, password, message):
        time.sleep(10)
        self.driver.get(url="https://x.com")
        self.driver.maximize_window()
        time.sleep(3)
        welcome_close = self.driver.find_elements(By.CSS_SELECTOR, value='.css-175oi2r .r-2o02ov .css-175oi2r .r-1777fci')
        for x in welcome_close:
            x.click()
        time.sleep(5)
        login_window = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        time.sleep(5)
        login_window.send_keys(user, Keys.ENTER)
        time.sleep(5)
        password_window = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_window.send_keys(password, Keys.ENTER)
        time.sleep(10)
        comment_window = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div')
        comment_window.click()
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(message)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span')
        post_button.click()

    def close(self):
        self.driver.quit()