# with open("./weather_data.csv") as data:
#     weather_reports = data.readlines()
#     print(weather_reports)
#     for weather in weather_reports:
#         strip_data = weather.strip()
#         print(strip_data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Using panda
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
# # Data Frames and Series:
# print(type(data))
# print(type(data["temp"]))

# Data to dic

# data_dict = data.to_dict()
# print(data_dict)

# Data to list

# data_list = data["temp"].to_list()
# print(data_list)
# avg = sum(data_list)/len(data_list)
# print(avg)

# In Data Series Computation
# print("Average Temperature :", data["temp"].mean())
#
# print("Average Temperature :", data["temp"].max())

# Easy method to call data
# print(data.day)
# print(data.condition)

# Get row data

# print(data[data.day == "Monday"])

# Get the max temp
# print(data[data.temp == data["temp"].max()])

# To get the particular value
# sunday = data[data.day == "Sunday"]
# sun_temp = sunday.temp
# print(sun_temp)
# # To convert Celsius to Fahrenheit for Monday
# Fahrenheit = 9/5 * sun_temp + 32
# print(Fahrenheit)

# Create a Data Frame from Scratch

# data_dict = {
#     "Students": ["Kishore", "Karthik", "Vasanthan"],
#     "Score": [95, 80, 90]
# }
# # DataFrame
# data_d = pandas.DataFrame(data_dict)
# print(data_d)
# # Convert and create the file
# data_d.to_csv("New Data.csv")

import pandas

# My method
# data_squirrel = pandas.read_csv("Squirrel_Data.csv")
# # print(data_squirrel)
# # print(data_squirrel["Primary Fur Color"])
# # print(data_squirrel.Location)
#
# # Count the fur color of individual squirrel
# color = (data_squirrel.value_counts("Primary Fur Color"))
#
# squ_color = pandas.DataFrame(color)
# print(squ_color)
# squ_color.to_csv("color_squirrel.csv")

# Actual method
data = pandas.read_csv("Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_count)
# print(red_count)
# print(black_count)

# fit into dict
data_dict = {
    "Fur color": ["Grey", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("Squirrel_count.csv")


