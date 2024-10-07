import requests
from twilio.rest import Client
Weather = "https://api.openweathermap.org/data/2.5/forecast"
Free_API_Key = "687fec0210cedcc33afc3d3cf3b96b16"
account_sid = "AC47bd692afb6a3a6f600cc63278568e3c"
auth_token = "7f46eb3c99316b57695744c83b5f04cb"


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
        from_="whatsapp:+14155238886",
        to="whatsapp:+18316010502",
    )
    print(message.status)
