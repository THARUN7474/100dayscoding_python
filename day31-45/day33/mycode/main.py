import requests

resp = requests.get(url="http://api.open-notify.org/iss-now.json")#api endpoint
print(resp)
# we get response code on api request request codes are example 1xx for holdon we get something, 2xx fr successfull
# request, 3xx go away no permission ,4xx we didnt have good request, we have aproblem client side , 5xx server side
# problem
print(resp.status_code)
# if resp.status_code != 200:
#     raise Exception("bad responce from ISS api")
#
# if resp.status_code == 404:
#     raise Exception("resource doesnot exist")
resp.raise_for_status()

data = resp.json()
print(data)
print(data.get("iss_position"))
print((data.get("iss_position").get("latitude"),data.get("iss_position").get("longitude")))
