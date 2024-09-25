# ui.py
import tkinter as tk
from datetime import datetime
import time
from weather_service import WeatherService

class WeatherApp:
    def __init__(self, master, weather_service):
        self.master = master
        self.weather_service = weather_service
        self.master.geometry("600x500")
        self.master.title("Weather App")
        self.create_widgets()

    def create_widgets(self):
        self.textField = tk.Entry(self.master, justify='center', width=20, font=("poppins", 35, "bold"))
        self.textField.pack(pady=20)
        self.textField.focus()
        self.textField.bind('<Return>', self.get_weather)

        self.label1 = tk.Label(self.master, font=("poppins", 35, "bold"))
        self.label1.pack()
        self.label2 = tk.Label(self.master, font=("poppins", 15, "bold"))
        self.label2.pack()

    def get_weather(self, event):
        city = self.textField.get()
        if not city:
            return

        try:
            json_data = self.weather_service.get_weather_data(city)
            weather_info = self.weather_service.parse_weather_data(json_data)

            sunrise = time.strftime('%I:%M:%S', time.gmtime(weather_info['sunrise'] - 21600))
            sunset = time.strftime('%I:%M:%S', time.gmtime(weather_info['sunset'] - 21600))

            final_info = f"{weather_info['condition']}\n{weather_info['temp']}°C"
            final_data = (f"\nMin Temp: {weather_info['min_temp']}°C\n"
                          f"Max Temp: {weather_info['max_temp']}°C\n"
                          f"Pressure: {weather_info['pressure']}\n"
                          f"Humidity: {weather_info['humidity']}\n"
                          f"Wind Speed: {weather_info['wind']}\n"
                          f"Sunrise: {sunrise}\n"
                          f"Sunset: {sunset}")
            
            self.label1.config(text=final_info)
            self.label2.config(text=final_data)

        except Exception as e:
             
            self.label1.config(text="Error fetching data")
            self.label2.config(text=str(e))
