import requests
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = #yourapikey
account_sid = #youraccountsid
auth_token = #yourtoken
weather_params = {
    "lat": 38.192329,
    "lon": 15.555520,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

will_rain = False
condition_code = data["weather"][0]["id"]
if int(condition_code) < 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's raining today.",
        from_= #phonenumber,
        to= #phonenumber
    )
    print(message.status)

