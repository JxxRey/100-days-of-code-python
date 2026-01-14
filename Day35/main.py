import requests
import os
from twilio.rest import Client



OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


parameters = {
"lat": 47.6062,
"lon": -122.3321,
"appid": api_key,
"cnt": 4,
"units": "metric"
}

response = requests.get(OWM_Endpoint, params=parameters)
print(response.status_code)
response.raise_for_status()

data = response.json()
print(data)


will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+18446702586",
        to="+17754210535"
    )
    print(message.status)







