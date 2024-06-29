import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 68
HEIGHT_CM = 178
AGE = 18
#above are extra things

api_id = "db2708c8"
api_key = "9cfb316ee0cb74516d94120023c491c6"
API_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_user_name = "tharunpython"
shetty_password = "123EWQ123EWQ!@#"
SHEETS_API_ENDPOINT = "https://api.sheety.co/524f6188ee06b9a0502b06b2aa3b17ec/workoutpython/workouts"

os.environ["APP_ID"] = api_id
os.environ["APP_KEY"] = api_key
os.environ["SHEET_ENDOINT"] = SHEETS_API_ENDPOINT
os.environ["SHEET_USER"] = shetty_user_name
os.environ["SHEET_PASS"] = shetty_password
headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["APP_KEY"]
}
param = {
    "query": input("enter what you did today"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
resp = requests.post(url=API_endpoint,headers=headers,data=param)
print(resp.json())
result = resp.json()

# or we c an use like this too
# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(result)




today_time = datetime.now().strftime("%X")
# print(today_time)
today_data = datetime.now().strftime("%d/%m/%Y")

for ex in result.get("exercises"):
    SHEET_params = {
        "workout": {
            "date": today_data,
            "time": today_time,
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"]
        }
    }


from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth(os.environ["SHEET_USER"],os.environ["SHEET_PASS"])



respp = requests.post(url=SHEETS_API_ENDPOINT,json=SHEET_params,auth=basic)
print(respp.json())