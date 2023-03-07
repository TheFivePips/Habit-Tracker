import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": config["PIXELA_TOKEN"],
    "username": "thefivepips",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# created a user name and password
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
