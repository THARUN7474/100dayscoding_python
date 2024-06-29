import requests
from datetime import datetime


username = "tharun747474"
TOKEN = "tharun747474@123457"
headers = {
    "X-USER-TOKEN": TOKEN
}


pixela_endpoint = "https://pixe.la/v1/users"
paras_user = {
    "token" : "tharun747474@123457",
    "username": "tharun747474",
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}
# resp = requests.post(url=pixela_endpoint,json=paras_user)
# print(resp.json())
# print(resp.text)#these steps are for creating a user id in that api so run only once if you change anything then new user will be created

#creating tracking graph
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_para = {
    "id": "graph1",
    "name": "running Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
resp =requests.post(url=graph_endpoint, json=graph_para, headers=headers)
print(resp.json())


#adding a pixel here
pixel_endpoint = "https://pixe.la/v1/users/tharun747474/graphs/graph1"
today = datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_para = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many km you ran today!"),
}
resp = requests.post(url=pixel_endpoint,json=pixel_para,headers=headers)
print(resp.json())

#updating pixel
update_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5"
}
## PUT
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)


delete_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today.strftime('%Y%m%d')}"
## DELETE
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

#goto this page to see results == https://pixe.la/v1/users/tharun747474/graphs/graph1.html

#further chances to improve
#we can make ui for this using tk module
#adding oops concept to encapusle evrything
#we can make it user friendly by showing results automatically as they enter the req input

