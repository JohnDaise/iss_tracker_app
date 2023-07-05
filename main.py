import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 38.955944
MY_LONG = -76.945534
# TEST
# MY_LAT = -31.955944
# MY_LONG = 22.945534
MY_EMAIL = "johnedaise@gmail.com"
PASSWORD = "iclvuycjrvtywpbu"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_latitude)
print(iss_longitude)


def see_if_iss_nearby():
    # see if position is within +5 or -5 degrees of the ISS position.
    if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LONG <= iss_longitude+5:
        return True


def see_if_currently_dark():
    if time_now.hour <= sunset or time_now.hour >= sunset:
        return True


def send_email_notification():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: LOOK UP!\n\n The ISS is in the sky. Look up!"
        )


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

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if see_if_currently_dark() and see_if_iss_nearby():
        # print("send email")
        send_email_notification()
    # else:
    #     print("not nearby and/or is dark")



