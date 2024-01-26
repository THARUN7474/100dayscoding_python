# #here open excel write a table form data and download as CSV form comma separated variable
# #And open using files concept and csv module and using pandas too
#
#
# #Using file methods
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# #using csv
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)
#
# # Using the pandas library
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
#
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # Get Row data value
# monday = data[data.day == "Monday"]#everything here it is as string so remember
# monday_temp = int(monday.temp)#monday.temp[0] can be used
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squrrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squrrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squrrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squrrels)#try using count method too
print(red_squrrels)#try using count method too
print(black_squrrels)#try using count method too

dict_ = {
    "FUR colour": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squrrels, red_squrrels, black_squrrels]
}

df = pandas.DataFrame(dict_)
df.to_csv("squrals.csv")