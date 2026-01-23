#This class is responsible for talking to the Flight Search API.
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
        self.amadeus_token = self.get_new_token()


    def get_new_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_api_key,
            "client_secret": self.amadeus_api_secret
        }

        response = requests.post(url=token_endpoint, headers=headers, data=body)
        return response.json()["access_token"]



    def get_iata_code(self, city_name):
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {
            "Authorization": f"Bearer {self.amadeus_token}"
        }
        params = {
            "keyword": city_name,
            "max": 2
        }
        response = requests.get(url=endpoint, headers=headers, params=params)

        try:
            code = response.json()["data"][0]["iataCode"]
        except (IndexError, KeyError):
            print(f"No Iata code found for {city_name}")
            return "N/A"
        return code


    def check_flights(self, origin_code, destination_code):
        tomorrow = datetime.now() + timedelta(days=1)
        six_months = tomorrow + timedelta(days=6*30)

        departure_date = tomorrow.strftime("%Y-%m-%d")
        return_date = six_months.strftime("%Y-%m-%d")

        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        headers = {
            "Authorization": f"Bearer {self.amadeus_token}"
        }

        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "currencyCode": "GBP",
            "max": 10
        }
        print(f"Using token: {self.amadeus_token[:20]}...")
        print(f"Params: {params}")

        response = requests.get(url=endpoint, headers=headers, params=params)

        if response.status_code!= 200:
            print(f"Error: {response.json()}")
            return None

        return response.json()


    def parse_flight_data(self, flight_json):
        """Extract the cheapest flight from the API response"""
        try:
            flights = flight_json["data"]

            if not flights:
                return None

            cheapest_flight = flights[0]

            price = float(cheapest_flight["price"]["total"])
            origin = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = cheapest_flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
            out_date = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = cheapest_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            return FlightData(
                price=price,
                origin_airport=origin,
                destination_airport=destination,
                out_date=out_date,
                return_date=return_date
            )
        except (KeyError, IndexError, TypeError):
            return None