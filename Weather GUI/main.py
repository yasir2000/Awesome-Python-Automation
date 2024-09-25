# main.py
import os
import tkinter as tk
from weather_service import WeatherService
from ui import WeatherApp


def main():
    # Initialize the main Tkinter window
    root = tk.Tk()

    # Environment variable for the API key
    api_key = os.getenv('API_KEY')

    # Dependency Injection: Create WeatherService object
    weather_service = WeatherService(api_key)

    # Create WeatherApp instance
    app = WeatherApp(root, weather_service)
    
    # Start the tkinter loop
    root.mainloop()

if __name__ == "__main__":
    main()
