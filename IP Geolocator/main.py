import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_URL = os.getenv("API_URL")

# Define an interface for the Locator
class LocatorInterface:
    def locate(self, ip: str) -> dict:
        pass

# Implement the locator using the Factory Method pattern
class IpLocator(LocatorInterface):
    def locate(self, ip: str) -> dict:
        response = requests.get(f"{API_URL}{ip}").json()
        return response

# Service to handle geolocation
class GeolocationService:
    def __init__(self, locator: LocatorInterface):
        self.locator = locator

    def get_location(self, ip: str):
        result = self.locator.locate(ip)
        if result["status"] == "success":
            return {
                "IP": ip,
                "Country": result["country"],
                "Region": result["regionName"],
                "City": result["city"],
                "ZIP": result["zip"],
                "Latitude": result["lat"],
                "Longitude": result["lon"],
                "Timezone": result["timezone"],
                "ISP": result["isp"],
            }
        else:
            return None

# Command to encapsulate actions related to geolocation
class GeolocationCommand:
    def __init__(self, service: GeolocationService):
        self.service = service

    def execute(self, ip: str):
        location = self.service.get_location(ip)
        if location:
            print("Successfully Located :", location["IP"])
            for key, value in location.items():
                print(f"{key}: {value}")
        else:
            print("Error! Please try again.")

# Client code to interact with the user
if __name__ == "__main__":
    ip = input("Enter IP Address To Geolocate: ")
    ip_locator = IpLocator()
    geo_service = GeolocationService(locator=ip_locator)
    command = GeolocationCommand(service=geo_service)
    command.execute(ip)
