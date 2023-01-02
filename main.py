import requests
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "afa29fb6be8f9148477fdbb0a550ac41"
account_sid = "ACd559915cf718cb6b10b1a891d6657a11"
auth_token = "4f7345fc4f17a52a1a002086659acbd0"
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
        from_= "+14632555046",
        to= "+393518957923"
    )
    print(message.status)

