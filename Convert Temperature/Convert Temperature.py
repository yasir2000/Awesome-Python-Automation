import os
import math
from abc import ABC, abstractmethod

# Temperature Converter Base Class
class TemperatureConverter(ABC):
    @abstractmethod
    def convert(self, value):
        pass

# Celsius to other conversions
class CelsiusConverter(TemperatureConverter):
    def convert(self, value, to_unit):
        if to_unit == 'fahrenheit':
            return (value * (9 / 5)) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        raise ValueError("Unsupported conversion")

# Fahrenheit to other conversions
class FahrenheitConverter(TemperatureConverter):
    def convert(self, value, to_unit):
        if to_unit == 'celsius':
            return (value - 32) * (5 / 9)
        elif to_unit == 'kelvin':
            return (value - 32) * (5 / 9) + 273.15
        raise ValueError("Unsupported conversion")

# Kelvin to other conversions
class KelvinConverter(TemperatureConverter):
    def convert(self, value, to_unit):
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * (9 / 5) + 32
        raise ValueError("Unsupported conversion")

# TemperatureConversionFactory for creating converters
class TemperatureConversionFactory:
    @staticmethod
    def create_converter(from_unit):
        if from_unit == 'celsius':
            return CelsiusConverter()
        elif from_unit == 'fahrenheit':
            return FahrenheitConverter()
        elif from_unit == 'kelvin':
            return KelvinConverter()
        raise ValueError("Unsupported temperature unit")

# Environment Variable Setup (Create a .env file to specify)
def load_env():
    if not os.path.exists('.env'):
        with open('.env', 'w') as env_file:
            env_file.write('DEFAULT_UNIT=celsius\n')

def main():
    load_env()
    default_unit = os.getenv('DEFAULT_UNIT', 'celsius')

    from_unit = input("Select temperature to convert from (celsius, fahrenheit, kelvin): ") or default_unit
    to_unit = input("Select conversion temperature (celsius, fahrenheit, kelvin): ")
    value = float(input(f"Enter temperature in {from_unit}: "))

    converter = TemperatureConversionFactory.create_converter(from_unit)

    try:
        final_value = converter.convert(value, to_unit)
        print(f"The temperature is: {final_value:.2f} °{to_unit[0].upper()}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
