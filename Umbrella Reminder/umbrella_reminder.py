import schedule
import os
from umbrellaReminder import *
import smtplib
from dotenv import load_dotenv
load_dotenv()

class UmbrellaReminder:
    def __init__(self, city, weather_provider):
        self.city = city
        self.weather_provider = weather_provider

    def send_umbrella_reminder(self):
        weather_info = self.weather_provider.get_weather_info()

        if weather_info['sky'] in ["Rainy", "Rain And Snow", "Showers", "Haze", "Cloudy"]:
            smtp_object = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
            smtp_object.starttls()
            smtp_object.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

            subject = "Umbrella Reminder"
            body = f"Take an umbrella before leaving the house. Weather condition for today is {weather_info['sky']} and temperature is {weather_info['temperature']} in {self.city}."

            msg = f"Subject:{subject}\n\n{body}\n\nRegards".encode('utf-8')
            smtp_object.sendmail(os.getenv('FROM_EMAIL'), os.getenv('TO_EMAIL'), msg)
            smtp_object.quit()
            print("Email Sent!")

# Create the weather provider factory
weather_provider_factory = WeatherProviderFactory()

# Create an instance of the UmbrellaReminder class with weather provider injected
umbrella_reminder = UmbrellaReminder(os.getenv('CITY'), weather_provider_factory.get_provider(os.getenv('CITY')))
