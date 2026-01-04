# with open("./weather_data.csv") as weather_data:
#     unstripped_data = weather_data.readlines()
#     data = []
#     for line_of_data in unstripped_data:
#         stripped_data = line_of_data.strip()
#         data.append(stripped_data)
# print(data)

# import csv
# # with open("./weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)


import pandas

# CREATE VARIABLE WITH CSV FILE.
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# EXTRACT NUMBER OF SQUIRRELS FROM "PRIMARY FUR COLOR" COLUMN THAT ARE A SPECIFIC COLOR.
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

# CREATE DICTIONARY WITH THE DATA
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

# TURN DICTIONARY INTO DATAFRAME
df = pandas.DataFrame(data_dict)

# TURN DATAFRAME INTO A NEW CSV FILE
df.to_csv("squirrel_count.csv")


print(df)
