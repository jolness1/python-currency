import requests


def convert_currency(amount, start_currency, end_currency):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey={apikey}&base_currency={start_currency}&currencies={end_currency}"
    response = requests.get(
        url.format(apikey="fca_live_Rmp5gWHFF5juckEH9pHQrokJv83Cm2YYBhXLyUyv", start_currency=start_currency,
                   end_currency=end_currency))
    data = response.json()

    conversion_rate = data["data"][end_currency]
    converted_amount = amount * conversion_rate

    return converted_amount


if __name__ == "__main__":
    amount = 30
    start_currency = "USD"
    end_currency = "GBP"

    converted_amount = convert_currency(amount, start_currency, end_currency)

    print(f"{amount} {start_currency} is equal to {converted_amount} {end_currency}")