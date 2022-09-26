import os
import csv
import pandas
# Pandas -> python data analysis library

with open(f"{os.getcwd()}/files/csv/weather_data.csv") as file:
  data = csv.reader(file)
  # data = file.readlines()
  tempratures = []
  for row in data:
    if row[1] != "temp":
      tempratures.append(int(row[1]))
  # print(tempratures)

data = pandas.read_csv(f"{os.getcwd()}/files/csv/weather_data.csv")
print(data)
