import requests
# from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_APIKEY = "CYSO1D8EF961V9R5"
news_apikey = "57519c29679c4e9b95c482f5c926b0ac"

key_id = "AC291a5ef43f3693c7ac2cca77e7f174f8"
key_auth = "3219c4b1c61d4866d6de41ac5ecbec42"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_para = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_APIKEY,
}

response = requests.get(url=STOCK_ENDPOINT,params=stock_para)
response.raise_for_status()
data = response.json()

stock_data = data["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
# print(stock_data_list)
# print(stock_data)
yesterday_closing_price = stock_data_list[0]["4. close"]
day_before_yesterday_closing_price = stock_data_list[1]["4. close"]

diff_closing = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
# print(diff_closing)
diff_prize = (diff_closing/float(yesterday_closing_price))*100
print(diff_prize)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if diff_prize > 1:
    # print("get news")
    para_news = {
        "q": "Apple",
        "qInTitle": COMPANY_NAME,
        # "from": "2024 - 02 - 14",
        # "sortBy": "popularity",
        "apiKey":news_apikey,
    }
    resp = requests.get(url=NEWS_ENDPOINT,params=para_news)
    resp.raise_for_status()
    # print(resp.json())
    articles = resp.json()["articles"]
    # print(articles)
    # print(articles[:3])
    final_news = articles[:3]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

list_news = [f"{STOCK}:{int(diff_prize)} \nheadline: {article['title']} \nBrief: {article['description']}" for article in final_news]
print(list_news)

client = Client(key_id, key_auth)
for arti in list_news:
    message = client.messages.create(
            body= arti,
            from_='+15077065269',
            to='+919381697664'
        )
    print(message.status)




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

