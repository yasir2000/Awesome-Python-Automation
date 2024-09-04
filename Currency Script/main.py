from converter import CurrencyConverter

def main():
    converter = CurrencyConverter()

    base_currency = input("Enter base currency (e.g., usd, eur): ").lower()

    while True:
        target_currency = input("Enter target currency to exchange to (empty to exit): ").lower()
        if not target_currency:
            break
        amount = int(input("Enter amount to exchange: "))
        result = converter.convert(base_currency, target_currency, amount)
        print(f"Converted amount: {result} {target_currency.upper()}.")

if __name__ == "__main__":
    main()
