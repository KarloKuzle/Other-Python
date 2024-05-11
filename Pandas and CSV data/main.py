
# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data)) -> DataFrama
# print(type(data["temp"])) -> Series

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# ili
avg_temp = data["temp"].mean()
max_temp = data["temp"].max()

# Get Data in Columns
# pandas has also converted every column name to an attribute
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()]) -> row where the temp was max

monday = data[data.day == "Monday"]
# print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32


# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


