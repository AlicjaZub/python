import requests
from datetime import datetime

USERNAME = "alicja"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
NEW_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
TOKEN = "pixela12345pixela109876"

headers = {
  "X-USER-TOKEN": TOKEN
}

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_params = {
  "id": "graph1",
  "name": "Python Graph",
  "unit": "min",
  "type": "float",
  "color": "kuro",
}

# response = requests.post(url=NEW_GRAPH_ENDPOINT, json=graph_params, headers=headers)

# today = datetime(year=2020, month=2, day=23)
today = datetime.now().strftime("%Y%m%d")

pixel_params = {
  "date": today,
  "quantity": input("How many minutes of Python have you studied today? "),
}

response = requests.post(url=GRAPH_ENDPOINT, json=pixel_params, headers=headers)
print(response.text)