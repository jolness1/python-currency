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

CURRENCY_SYMBOLS = {
    "EUR": "€",
    "USD": "$",
    "JPY": "¥",
    "BGN": "лв",
    "CZK": "Kč",
    "DKK": "kr",
    "GBP": "£",
    "HUF": "Ft",
    "PLN": "zł",
    "RON": "lei",
    "SEK": "kr",
    "CHF": "Fr",
    "ISK": "kr",
    "NOK": "kr",
    "HRK": "kn",
    "RUB": "₽",
    "TRY": "₺",
    "AUD": "$",
    "BRL": "R$",
    "CAD": "$",
    "CNY": "¥",
    "HKD": "HK$",
    "IDR": "Rp",
    "ILS": "₪",
    "INR": "₹",
    "KRW": "₩",
    "MXN": "$",
    "MYR": "RM",
    "NZD": "NZ$",
    "PHP": "₱",
    "SGD": "S$",
    "THB": "฿",
    "ZAR": "R",
}

COUNTRY_TO_CURRENCY = {
    "austria": "EUR",
    "belgium": "EUR",
    "croatia": "EUR",
    "cyprus": "EUR",
    "estonia": "EUR",
    "finland": "EUR",
    "france": "EUR",
    "germany": "EUR",
    "greece": "EUR",
    "ireland": "EUR",
    "italy": "EUR",
    "latvia": "EUR",
    "lithuania": "EUR",
    "luxembourg": "EUR",
    "malta": "EUR",
    "netherlands": "EUR",
    "portugal": "EUR",
    "slovakia": "EUR",
    "slovenia": "EUR",
    "spain": "EUR",
    "united states": "USD",
    "japan": "JPY",
    "bulgaria": "BGN",
    "czech republic": "CZK",
    "denmark": "DKK",
    "united kingdom": "GBP",
    "hungary": "HUF",
    "poland": "PLN",
    "romania": "RON",
    "sweden": "SEK",
    "switzerland": "CHF",
    "iceland": "ISK",
    "norway": "NOK",
    "russia": "RUB",
    "turkey": "TRY",
    "australia": "AUD",
    "brazil": "BRL",
    "canada": "CAD",
    "china": "CNY",
    "hong kong": "HKD",
    "indonesia": "IDR",
    "israel": "ILS",
    "india": "INR",
    "south korea": "KRW",
    "mexico": "MXN",
    "malaysia": "MYR",
    "new zealand": "NZD",
    "philippines": "PHP",
    "singapore": "SGD",
    "thailand": "THB",
    "south africa": "ZAR",
}


def get_currency_code(name, country_to_currency):
    return country_to_currency.get(name.lower(), name).upper()


def generate_conversion_message(amount, start_currency, end_currency, converted_amount):
    return f"{CURRENCY_SYMBOLS.get(start_currency)}{amount} {start_currency} is equal to {CURRENCY_SYMBOLS.get(end_currency)}{converted_amount} {end_currency}"


def convert_currency(amount, start_currency, end_currency, country_to_currency):
    try:
        # Convert country names to currency codes
        start_currency = get_currency_code(start_currency, country_to_currency)
        end_currency = get_currency_code(end_currency, country_to_currency)

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
            raise Exception(
                f"Failed to convert currency: {response.status_code} {response.reason}")

        conversion_rate = data["data"][end_currency]
        converted_amount = round(amount * conversion_rate, 2)
        message = generate_conversion_message(
            amount, start_currency, end_currency, converted_amount)
        return message

    except ValueError as ve:
        message = f"ValueError: {ve}"
        print(message)
        return None
    except Exception as e:
        message = f"An unexpected error occurred: {e}"
        print(message)
        raise


def list_currencies():
    print("Available currency abbreviations and their full names:")
    for code, name in CURRENCY_CODES.items():
        print(f"{code}\t{name}")


def main():
    parser = argparse.ArgumentParser(description="Convert currency using FreeCurrencyAPI",
                                     usage="currency_converter.py [amount] [start_country] [end_country]"
                                     )
    parser.add_argument("amount", type=float, nargs="?",
                        help="Amount to convert")
    parser.add_argument("start_country", type=str, nargs="?",
                        help="Home country name (e.g., Germany)")
    parser.add_argument("end_country", type=str, nargs="?",
                        help="Converted country name (e.g., France)")
    parser.add_argument('--list-currencies', '-lc', action="store_true",
                        help="List available currency abbreviations and exit")

    args = parser.parse_args()

    if args.list_currencies:
        list_currencies()
        return

    if not args.amount:
        args.amount = float(input("Enter the amount to convert: "))
    if not args.start_country:
        args.start_country = input(
            "Enter the home country name or currency code (e.g., Germany or EUR): ")
    if not args.end_country:
        args.end_country = input(
            "Enter the converted country name or currency code (e.g., France or EUR): ")

    start_currency = get_currency_code(args.start_country, COUNTRY_TO_CURRENCY)
    end_currency = get_currency_code(args.end_country, COUNTRY_TO_CURRENCY)

    conversion_result = convert_currency(
        args.amount, args.start_country, args.end_country, COUNTRY_TO_CURRENCY)

    if conversion_result is not None:
        print(conversion_result)
    else:
        print("Conversion failed.")


if __name__ == "__main__":
    main()
