<<<<<<< HEAD
import requests
from datetime import datetime
#import os

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 162
AGE = 23

API_ID = "7f4d95d7" #os.environ["7f4d95d7"]
API_KEY = "09af96969d28173ed5a25e68e8ce723e"       #os.environ["09af96969d28173ed5a25e68e8ce723e"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

text_the_exercise = input("Tell me what exercise you did:")

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameter = {
    "query": text_the_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameter, headers=header)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

today = datetime.now().strftime("%d%m%y")
# print(today)
now = datetime.now().strftime("%X")
# print(now)

# Sheety

GOOGLE_SHEET_NAME = "sheet1"

sheety_endpoint = 'https://api.sheety.co/4a47506bc7d9b9a58b98c31aa64929b4/myWorkoutsTracking/sheet1' #os.environ['https://api.sheety.co/4a47506bc7d9b9a58b98c31aa64929b4/myWorkoutsTracking/sheet1']

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

# payload = {
#     "sheet1": sheet_inputs
# }

SHEETY_TOKEN = "Rmlib246KGZpYm9uYWNjKm9kZXIp" #os.environ["Rmlib246KGZpYm9uYWNjKm9kZXIp"]

# Barer Token

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

sheet_response = requests.post(sheety_endpoint,
                               json=sheet_inputs,
                               headers=bearer_headers)

print(f"Sheety Response: \n {sheet_response.text}")



# sheet_response_get = requests.get(sheety_endpoint,
#                                   json=payload,
#                                   headers=bearer_headers)
# print(sheet_response_get.text)

# APP_ID = os.environ["APP_ID"] – raises exception if key does not exist
# APP_ID = os.environ.get("APP_ID") – returns None if key does not exist
# APP_ID = os.environ.get("APP_ID", “Message”) – returns “Message” if key does not exist

# API_ID = "7f4d95d7"
# API_KEY = "09af96969d28173ed5a25e68e8ce723e"
# SHEETY_TOKEN = "Rmlib246KGZpYm9uYWNjKm9kZXIp"
# sheety_endpoint = 'https://api.sheety.co/4a47506bc7d9b9a58b98c31aa64929b4/myWorkoutsTracking/sheet1'
=======
import requests
from datetime import datetime
#import os

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 162
AGE = 23

API_ID = "7f4d95d7" #os.environ["7f4d95d7"]
API_KEY = "09af96969d28173ed5a25e68e8ce723e"       #os.environ["09af96969d28173ed5a25e68e8ce723e"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

text_the_exercise = input("Tell me what exercise you did:")

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameter = {
    "query": text_the_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameter, headers=header)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

today = datetime.now().strftime("%d%m%y")
# print(today)
now = datetime.now().strftime("%X")
# print(now)

# Sheety

GOOGLE_SHEET_NAME = "sheet1"

sheety_endpoint = 'https://api.sheety.co/4a47506bc7d9b9a58b98c31aa64929b4/myWorkoutsTracking/sheet1' #os.environ['https://api.sheety.co/4a47506bc7d9b9a58b98c31aa64929b4/myWorkoutsTracking/sheet1']

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

# payload = {
#     "sheet1": sheet_inputs
# }

SHEETY_TOKEN = "Rmlib246KGZpYm9uYWNjKm9kZXIp" #os.environ["Rmlib246KGZpYm9uYWNjKm9kZXIp"]

# Barer Token

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

sheet_response = requests.post(sheety_endpoint,
                               json=sheet_inputs,
                               headers=bearer_headers)

print(f"Sheety Response: \n {sheet_response.text}")



# sheet_response_get = requests.get(sheety_endpoint,
#                                   json=payload,
#                                   headers=bearer_headers)
# print(sheet_response_get.text)

# APP_ID = os.environ["APP_ID"] – raises exception if key does not exist
# APP_ID = os.environ.get("APP_ID") – returns None if key does not exist
# APP_ID = os.environ.get("APP_ID", “Message”) – returns “Message” if key does not exist

# API_ID = "7f4d95d7"
# API_KEY = "09af96969d28173ed5a25e68e8ce723e"
# SHEETY_TOKEN = "Rmlib246KGZpYm9uYWNjKm9kZXIp"
# sheety_endpoint = 'https://api.sheety.co/4a47506bc7d9b9a58b98c31aa64929b4/myWorkoutsTracking/sheet1'
>>>>>>> 54efe6e67173470a814e51c6d84ea55a45fb80e5
