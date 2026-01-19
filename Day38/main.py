import requests
import os
from datetime import datetime

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/2a19b19fc6236347e395007674ef6564/workoutTracking/workouts"

exercise_text = input("What workout did you do?")

headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
}

body = {
"query": exercise_text,
}

response = requests.post(url=exercise_endpoint, json=body, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
    "workout": {
    "date": today_date,
    "time": now_time,
    "exercise": exercise["name"].title(),
    "duration": exercise["duration_min"],
    "calories": exercise["nf_calories"]
    }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_headers)

    print(sheet_response.text)