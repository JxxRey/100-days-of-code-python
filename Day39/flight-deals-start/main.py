# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "RNO"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

for city in sheet_data:
    if not city["iataCode"]:
        city_name = city["city"]
        iata_code = flight_search.get_iata_code(city_name)
        city["iataCode"] = iata_code
        data_manager.update_destination_codes(city["id"], iata_code)

# Search for flights and check for deals
for destination in sheet_data:
    print(f"\nChecking flights for {destination['city']}...")

    flights_json = flight_search.check_flights(
        origin_code=ORIGIN_CITY_IATA,
        destination_code=destination["iataCode"]
    )

    if flights_json:
        flight = flight_search.parse_flight_data(flights_json)

        if flight:
            print(f"Found flight: £{flight.price}")

            if flight.price < destination["lowestPrice"]:
                message = (
                    f"Low price alert! Only £{flight.price} to fly from "
                    f"{flight.origin_airport} to {flight.destination_airport}, "
                    f"departing {flight.out_date} and returning {flight.return_date}."
                )
                notification_manager.send_notification(message)
            else:
                print(f"No deal - £{flight.price} vs target £{destination['lowestPrice']}")
        else:
            print("No flights found in response")
    else:
        print("API request failed")

print("\n✅ Flight search complete!")

#  Test email notification
notification_manager.send_notification("Test message - if you're reading this, email notifications work!")