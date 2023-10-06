import argparse

import requests

CURRENCY_CODES = {
    "EUR": "Euro",
    "USD": "US Dollar",
    "JPY": "Japanese Yen",
    "BGN": "Bulgarian Lev",
    "CZK": "Czech Republic Koruna",
    "DKK": "Danish Krone",
    "GBP": "British Pound Sterling",
    "HUF": "Hungarian Forint",
    "PLN": "Polish Zloty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "CHF": "Swiss Franc",
    "ISK": "Icelandic Króna",
    "NOK": "Norwegian Krone",
    "HRK": "Croatian Kuna",
    "RUB": "Russian Ruble",
    "TRY": "Turkish Lira",
    "AUD": "Australian Dollar",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CNY": "Chinese Yuan",
    "HKD": "Hong Kong Dollar",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "ZAR": "South African Rand",
}


def convert_currency(amount, start_currency, end_currency):
    try:
        if start_currency not in CURRENCY_CODES:
            raise ValueError(f"Invalid start currency: {start_currency}")
        if end_currency not in CURRENCY_CODES:
            raise ValueError(f"Invalid end currency: {end_currency}")

        url = "https://api.freecurrencyapi.com/v1/latest?apikey={apikey}&base_currency={start_currency}&currencies={end_currency}"
        response = requests.get(
            url.format(apikey="fca_live_Rmp5gWHFF5juckEH9pHQrokJv83Cm2YYBhXLyUyv", start_currency=start_currency,
                       end_currency=end_currency))
        data = response.json()

        if response.status_code != 200:
            raise Exception(f"Failed to convert currency: {response.status_code} {response.reason}")

        conversion_rate = data["data"][end_currency]
        converted_amount = amount * conversion_rate
        return converted_amount

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


def list_currencies():
    print("Available currency abbreviations and their full names:")
    for code, name in CURRENCY_CODES.items():
        print(f"{code}\t{name}")


def main():
    parser = argparse.ArgumentParser(description="Convert currency using FreeCurrencyAPI",
                                     usage="currency_converter.py [amount] [start_currency] [end_currency]"
                                     )
    parser.add_argument("amount", type=float, nargs="?", help="Amount to convert")
    parser.add_argument("start_currency", type=str, nargs="?", help="Home currency code (e.g., USD)")
    parser.add_argument("end_currency", type=str, nargs="?", help="Converted currency code (e.g., EUR)")
    parser.add_argument('--list-currencies', '-lc', action="store_true",
                        help="List available currency abbreviations and exit")

    args = parser.parse_args()

    if args.list_currencies:
        list_currencies()
        return

    if not args.amount:
        args.amount = float(input("Enter the amount to convert: "))
    if not args.start_currency:
        args.start_currency = input("Enter the home currency code (e.g., USD): ")
    if not args.end_currency:
        args.end_currency = input("Enter the converted currency code (e.g., EUR): ")

    converted_amount = convert_currency(args.amount, args.start_currency, args.end_currency)

    if converted_amount is not None:
        print(f"{args.amount} {args.start_currency} is equal to {converted_amount} {args.end_currency}")
    else:
        print("Conversion failed.")


if __name__ == "__main__":
    main()
