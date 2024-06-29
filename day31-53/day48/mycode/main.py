import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# # driv = webdriver.chrome
# driver = webdriver.chrome()
# driver.get("https://www.amazon.com")
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os
# chrome_driver_path = ".\Users\Tharun\Desktop\skills & me\L01_PYTHON_files\PycharmProjects\day31\.venv\Lib\site-packages\selenium"
# os.chmod(chrome_driver_path, 0o755)
# service = ChromeService(executable_path=)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)#for having the site on untill we close
URL = "https://www.amazon.in/Apple-2022-10-9-inch-iPad-Wi-Fi/dp/B0BJMSFMHH/ref=sr_1_1_sspa?crid=6C2N03ICQLTR&dib=eyJ2IjoiMSJ9.iKOwXr2WsIw3vDGNmi5GTU-BEiPYYXPDdTqeOeb835hJQ1VfEWQag3ekAbTnKFVxVQLVQeIhDnqx7tJ2M5WwtCOjVRQ_F7czh7FBypDuDMoraCreAlVhshITOdcFkGiXsZqTjFasap_iDY5zEkU0M7eR1sYYmDmA2WCVa2wntzdQfF_YC4Zj65XXnH8t1wyQGPtL68_BtYyC-EWR9aElf3rmaA7op4YuSOzF1tzy1z8.F27nek2mCGbkXF2A3rmaXIHlU2LCwUbR0X0rmfcExFI&dib_tag=se&keywords=ipad+10th+generation&qid=1709960073&sprefix=ipad+%2Caps%2C230&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"



driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
#here seleium used to automate flow of browser work

#to get precise element text here for price

price_money = driver.find_element(By.CLASS_NAME , value="a-price-whole")

print(f"The prize of ipad is {price_money}")

price_money = driver.find_element(By.ID , value="a-price-whole").text
price_money = driver.find_element(By.NAME , value="a-price-whole").size
price_money = driver.find_element(By.CSS_SELECTOR, value="div p a").get_attribute("placeholder")
#above all are diffr methods to get element details as without .text all those it pnly give selenium object type

#Xpaths like     html/body/div/p/a---like this ---copy paste from insepct only
price_money = driver.find_element(By.XPATH, value="html/body/div/p/a").get_attribute("placeholder")

# driver.close()
driver.quit()