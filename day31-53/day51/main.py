import os
import time
from  Speedtwitterbot import InternetSpeedTwitterBot

PROMISED_UP = 1000
PROMISED_DOWN = 1000
TWITTER_USERNAME = os.environ.get("USERNAME")
TWITTER_PASSWORD = os.environ.get("PASSWORD")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
time.sleep(10)

if PROMISED_UP > bot.up or PROMISED_DOWN > bot.down:
    message = f"Hey Internet Provider, why is my internet speed {bot.down}down/{bot.up}up when I pay for 1000down/1000up?"
    bot.tweet_at_provider(password=TWITTER_PASSWORD, user=TWITTER_USERNAME, message=message)

bot.close()