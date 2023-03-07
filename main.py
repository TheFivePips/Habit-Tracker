
from datetime import datetime

import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
token = config["PIXELA_TOKEN"]
username = config["PIXELA_USERNAME"]
graph_ID = config["PIXELA_GRAPH_ID"]
graph_name = config["PIXELA_GRAPH_NAME"]

today = datetime.now()


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# created a user name and password
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": graph_ID,
    "name": "Studying Graph",
    "unit": "Hours",
    "type": "int",
    "color": "sora"
}
graph_headers = {
    "X-USER-TOKEN": token
}
#created the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(response.text)

place_pixel_endpoint = f"{graph_endpoint}/{graph_ID}"

place_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? ")
}
response = requests.post(url=place_pixel_endpoint, json=place_pixel_config, headers=graph_headers)
print(response.text)


update_endpoint = f"{place_pixel_endpoint}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "0"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=graph_headers)
# print(response.text)


delete_endpoint = f"{place_pixel_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=graph_headers)
# print(response.text)
