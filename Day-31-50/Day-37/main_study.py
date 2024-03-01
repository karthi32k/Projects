<<<<<<< HEAD
# Habit Tracking Project
# Using Japanese API

import requests
from datetime import datetime

TOKEN = "qwerasdfzxcvjkluionm"
USERNAME = "karthik"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#NEW_TOKEN = 'https://pixe.la/v1/users/USERNAME/"qwerasdfzxcvjkluionm"/'{"poiurewq123ty098":"poiurewq123ty098"}''
# NEW_TOKEN = "poiurewq123ty098"
#
# header = {
#     'X-USER-TOKEN': NEW_TOKEN,
# }
#
# Update_token ={
#     "token": TOKEN,
#     "newToken": NEW_TOKEN,
# }
#
# upd_tkn = requests.put(url=f"{pixela_endpoint}/{USERNAME}", json=Update_token, headers=header)
# print(upd_tkn.text)

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# Create Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter = {
    "id": GRAPH_ID,
    "name": "Python Learning Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

header = {
    'X-USER-TOKEN': TOKEN,
}

# response_graph = requests.post(url=graph_endpoint, json=graph_parameter, headers=header)
# print(response_graph.text)

# Post the  PIXEL into graph

post_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%y%m%d"))

post_pixel_parameter = {
    "date": today.strftime("%y%m%d"),
    "quantity": input("How many hours did you study today?"),
}

# response_post_graph = requests.post(url=post_pixel, json=post_pixel_parameter, headers=header)
# print(response_post_graph.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%y%m%d')}"

new_pixel_data = {
    "quantity": "2.5",
}

#PUT
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
print(response.text)
=======
# Habit Tracking Project
# Using Japanese API

import requests
from datetime import datetime

TOKEN = "qwerasdfzxcvjkluionm"
USERNAME = "karthik"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#NEW_TOKEN = 'https://pixe.la/v1/users/USERNAME/"qwerasdfzxcvjkluionm"/'{"poiurewq123ty098":"poiurewq123ty098"}''
# NEW_TOKEN = "poiurewq123ty098"
#
# header = {
#     'X-USER-TOKEN': NEW_TOKEN,
# }
#
# Update_token ={
#     "token": TOKEN,
#     "newToken": NEW_TOKEN,
# }
#
# upd_tkn = requests.put(url=f"{pixela_endpoint}/{USERNAME}", json=Update_token, headers=header)
# print(upd_tkn.text)

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# Create Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter = {
    "id": GRAPH_ID,
    "name": "Python Learning Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

header = {
    'X-USER-TOKEN': TOKEN,
}

# response_graph = requests.post(url=graph_endpoint, json=graph_parameter, headers=header)
# print(response_graph.text)

# Post the  PIXEL into graph

post_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%y%m%d"))

post_pixel_parameter = {
    "date": today.strftime("%y%m%d"),
    "quantity": input("How many hours did you study today?"),
}

# response_post_graph = requests.post(url=post_pixel, json=post_pixel_parameter, headers=header)
# print(response_post_graph.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%y%m%d')}"

new_pixel_data = {
    "quantity": "2.5",
}

#PUT
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
print(response.text)
>>>>>>> 54efe6e67173470a814e51c6d84ea55a45fb80e5
