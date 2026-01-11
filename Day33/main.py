import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "Unfinished"
MY_PASSWORD = "Unfinished"
MY_LAT = 38.80
MY_LNG = -116.41


def is_iss_overhead():
    """Check if ISS is within 5 degrees of my position"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is within +5 or -5 degrees
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5):
        return True
    return False


def is_dark():
    """Check if it's nighttime (before sunrise or after sunset)"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "tzid": "America/Los_Angeles",
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    # Check if current time is before sunrise or after sunset
    if current_hour < sunrise or current_hour >= sunset:
        return True
    return False


def send_email():
    """Send email notification to look up at the ISS"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up! ☝️\n\nThe ISS is above you in the sky right now!"
        )


# Main loop - check every 60 seconds
while True:
    if is_iss_overhead() and is_dark():
        print("ISS is overhead and it's dark - sending email!")
        send_email()
    else:
        print("Conditions not met - checking again in 60 seconds...")

    time.sleep(60)  # Wait 60 seconds before checking again