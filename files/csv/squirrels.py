import os
import pandas


data = pandas.read_csv(f"{os.getcwd()}/files/csv/squirrels.csv")

print(data["Primary Fur Color"])
  
# gray = 0
# cinnamon = 0
# black = 0

# for colour in data["Primary Fur Color"].to_list():
#   if colour == "Gray":
#     gray += 1
#   elif colour == "Black":
#     black += 1
#   elif colour == "Cinnamon":
#     cinnamon += 1
    
# print(gray)
# print(cinnamon)
# print(black)
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

colours_dict = {
  "Fur Colour": ["gray","black","cinnamon"],
  "Count": [gray, black, cinnamon],

}

data = pandas.DataFrame(colours_dict)
data.to_csv(f"{os.getcwd()}/files/csv/squirrels_colours.csv")