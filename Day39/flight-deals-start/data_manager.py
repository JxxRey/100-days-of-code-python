#This class is responsible for talking to the Google Sheet.
from dotenv import load_dotenv
import os
import requests

load_dotenv()



class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/2a19b19fc6236347e395007674ef6564/flightDeals/prices"
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")

    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, auth=(self.username, self.password))
        data = response.json()
        return data["prices"]




    def update_destination_codes(self, row_id, iata_code):
        sheety_endpoint = f"{self.SHEETY_ENDPOINT}/{row_id}"
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(
            url=sheety_endpoint,
            json=body,
            auth=(self.username, self.password)
        )
        return response
