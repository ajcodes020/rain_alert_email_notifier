import requests
import smtplib

MY_EMAIL = " Your Email "
MY_PASSWORD = " Your App Password"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = " Your API Key "

LATITUDE = " Your Latitude "
LONGITUDE = " Your Longitude "

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:Bring an umbrella!\n\nIt will rain in the next 12 hours."
        )