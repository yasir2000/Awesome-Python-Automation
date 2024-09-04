from currency import RateProvider, CurrencyAdapter

class CurrencyConverter:
    def __init__(self):
        self.rate_provider = RateProvider()
        self.adapter = CurrencyAdapter(self.rate_provider)

    def convert(self, from_currency, to_currency, amount):
        return self.adapter.convert(from_currency, to_currency, amount)

