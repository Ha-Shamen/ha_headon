import os
import requests


@staticmethod
def get_weather(lat: float, lon: float) -> float:
  # should be placed somewhere else
  app_id = os.environ.get("OPENWEATHER_API")
  owm_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={app_id}"
  owm_response = requests.get(owm_url)
  owm_response_json = owm_response.json()
  # convert temperature from Kelvin into centigrade
  return owm_response_json["main"]["temp"] - 273.15