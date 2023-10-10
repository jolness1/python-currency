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

COUNTRY_TO_CURRENCY = {
    "Austria": "EUR",
    "Belgium": "EUR",
    "Croatia": "EUR",
    "Cyprus": "EUR",
    "Estonia": "EUR",
    "Finland": "EUR",
    "France": "EUR",
    "Germany": "EUR",
    "Greece": "EUR",
    "Ireland": "EUR",
    "Italy": "EUR",
    "Latvia": "EUR",
    "Lithuania": "EUR",
    "Luxembourg": "EUR",
    "Malta": "EUR",
    "Netherlands": "EUR",
    "Portugal": "EUR",
    "Slovakia": "EUR",
    "Slovenia": "EUR",
    "Spain": "EUR",
    "United States": "USD",
    "Japan": "JPY",
    "Bulgaria": "BGN",
    "Czech Republic": "CZK",
    "Denmark": "DKK",
    "United Kingdom": "GBP",
    "Hungary": "HUF",
    "Poland": "PLN",
    "Romania": "RON",
    "Sweden": "SEK",
    "Switzerland": "CHF",
    "Iceland": "ISK",
    "Norway": "NOK",
    "Russia": "RUB",
    "Turkey": "TRY",
    "Australia": "AUD",
    "Brazil": "BRL",
    "Canada": "CAD",
    "China": "CNY",
    "Hong Kong": "HKD",
    "Indonesia": "IDR",
    "Israel": "ILS",
    "India": "INR",
    "South Korea": "KRW",
    "Mexico": "MXN",
    "Malaysia": "MYR",
    "New Zealand": "NZD",
    "Philippines": "PHP",
    "Singapore": "SGD",
    "Thailand": "THB",
    "South Africa": "ZAR",
}


def convert_currency(amount, start_currency, end_currency, country_to_currency):
    try:
        # If start_currency is a country name, map it to the currency code
        start_currency = country_to_currency.get(start_currency, start_currency)
        # If end_currency is a country name, map it to the currency code
        end_currency = country_to_currency.get(end_currency, end_currency)

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
                                     usage="currency_converter.py [amount] [start_country] [end_country]"
                                     )
    parser.add_argument("amount", type=float, nargs="?", help="Amount to convert")
    parser.add_argument("start_country", type=str, nargs="?", help="Home country name (e.g., Germany)")
    parser.add_argument("end_country", type=str, nargs="?", help="Converted country name (e.g., France)")
    parser.add_argument('--list-currencies', '-lc', action="store_true",
                        help="List available currency abbreviations and exit")

    args = parser.parse_args()

    if args.list_currencies:
        list_currencies()
        return

    if not args.amount:
        args.amount = float(input("Enter the amount to convert: "))
    if not args.start_country:
        args.start_country = input("Enter the home country name (e.g., Germany): ")
    if not args.end_country:
        args.end_country = input("Enter the converted country name (e.g., France): ")

    converted_amount = convert_currency(args.amount, args.start_country, args.end_country, COUNTRY_TO_CURRENCY)

    if converted_amount is not None:
        print(f"{args.amount} {args.start_country} is equal to {converted_amount} {args.end_country}")
    else:
        print("Conversion failed.")


if __name__ == "__main__":
    main()
