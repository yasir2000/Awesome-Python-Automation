# weather_service.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_data(self, city):
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(api_url)

        if response.status_code != 200:
            raise Exception(f"Error fetching weather data: {response.status_code}")

        return response.json()

    def parse_weather_data(self, json_data):
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = json_data['sys']['sunrise']
        sunset = json_data['sys']['sunset']
        
        return {
            "condition": condition,
            "temp": temp,
            "min_temp": min_temp,
            "max_temp": max_temp,
            "pressure": pressure,
            "humidity": humidity,
            "wind": wind,
            "sunrise": sunrise,
            "sunset": sunset
        }
