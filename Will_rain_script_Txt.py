import requests
from twilio.rest import Client
Weather = "https://api.openweathermap.org/data/2.5/forecast"
Free_API_Key = "<YOUR WEATHER KEY>"
account_sid = "<YOUR TWILIO KEY>"
auth_token = "<YOUR TWILIO AUTH TOKEN>"

# Coords currently set for Boise, ID
Weather_params = {
    "lat": 43.615021,
    "lon": -116.202316,
    "appid": Free_API_Key,
    "cnt": 4,
}

response = requests.get(Weather, Weather_params)
response.raise_for_status()
data = response.json()

rain = False
for hour in data["list"]:
    condition = hour["weather"][0]["id"]
    if int(condition) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella today!",
        from_="<YOUR TWILIO/WHATSAPP PHONE #>",
        to="<YOUR VERIFIED PHONE #>",
    )
    print(message.status)
