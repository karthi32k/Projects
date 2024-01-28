# Using through API to send SMS
import requests
import os
import vonage.client

api_key = os.environ.get("own_api_key")
authn_token = os.environ.get("auth_token")

owm_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_key = "8fd490d7926eb8c85d0d069898f25473"

parameters = {
    "lat": 11.652120,
    "lon": 78.157980,
    "appid": API_key,
    "cnt": 4,
}

response = requests.get(owm_Endpoint, params=parameters)
response.raise_for_status()
# print(response)

data = response.json()
# print(data)

# weather_data = data["list"][0]["weather"][0]["id"]
# print(weather_data)
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)
    if int(condition_code < 700):
        will_rain = True
    desc = hour_data["weather"][0]["description"]
    # print(desc)

if will_rain:
    # print("Hey, Don't forget to bring Umbrella☔")

    client = vonage.Client(key="233ec1c3", secret="hvweWeWuUARVdRI5")
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "919361263166",
            "text": f"Weather forecast:{desc}\n\nHey, Don't forget to bring Umbrella☔",
        }
    )
 
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
