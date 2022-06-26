import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 4.153740
MY_LONG = 9.243970
MY_EMAIL = "name@gmail.com"
MY_PASSWORD = "password"


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True


def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


# If the ISS is close to my current position, and it is currently dark
while True:
    time.sleep(60)
    if iss_close() and is_dark():
        print("Your position is within +5 or -5 degrees of the ISS position")
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="name2",
                msg="Subject:Look up!\n\nYour position is within +5 or -5 degrees of the ISS position."
            )
    else:
        print("Be patient")
