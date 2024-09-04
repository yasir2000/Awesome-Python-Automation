import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class RateProvider:
    """Singleton class to provide currency rates."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RateProvider, cls).__new__(cls)
            cls._instance.cache = {}
        return cls._instance

    def fetch_rates(self, currency):
        url = f"{os.getenv('API_URL')}/{currency}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        raise Exception("Failed to fetch exchange rates.")

    def get_rate(self, currency, target_currency):
        if currency not in self.cache:
            rates = self.fetch_rates(currency)
            self.cache.update({
                "usd": rates['usd']['rate'],
                "eur": rates['eur']['rate'],
                **{key: rates[key]['rate'] for key in rates if key not in ['usd', 'eur']}
            })
        return self.cache.get(target_currency)

class CurrencyAdapter:
    """Adapter for converting currency rates."""
    def __init__(self, currency_provider):
        self.currency_provider = currency_provider

    def convert(self, from_currency, to_currency, amount):
        rate = self.currency_provider.get_rate(from_currency, to_currency)
        if rate is None:
            return f"Exchange rate not found for {to_currency}."
        return round(amount * rate, 2)
