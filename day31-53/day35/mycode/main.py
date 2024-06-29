import requests
import os
from twilio.rest import Client

api_call = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "5f7599ac6ba0030aea64fa8eae511755"
my_lat = 17.385044
my_long = 78.486671

lat1 = 25.686613
lat2 = -100.316116

# -12.046373
# -77.042755#lima

key_id = "AC291a5ef43f3693c7ac2cca77e7f174f8"
key_auth = "3219c4b1c61d4866d6de41ac5ecbec42"

# account_sid = os.environ[key_id]
# auth_token = os.environ[key_auth]
# client = Client(account_sid, auth_token)


para ={
    "lat": lat1,
    "lon": lat2,
    "appid": api_key,
    "cnt":4,
}

responce = requests.get(url=api_call, params=para)
responce.raise_for_status()
# print(responce.status_code)
# print(responce.json())
weather_data = responce.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True
if will_rain:
    client = Client(key_id, key_auth)
    message = client.messages.create(
        body="its going to be rain please carry umberalla!!",
        from_='+15077065269',
        to='+919381697664'
    )

    print(message.status)