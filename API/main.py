import requests
from datetime import datetime
import time

MY_LAT = 45.592819
MY_LNG = 17.223890


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"] ["latitude"])

    iss_position = (iss_longitude, iss_latitude)

    # Your position is withing +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    res1 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    res1.raise_for_status()
    data1 = res1.json()
    sunrise = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data1["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour()

    if time_now >= sunset and time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        # send myself an email to look up!
        pass
