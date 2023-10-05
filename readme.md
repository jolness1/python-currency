# Currency Converter

A simple script for converting currencies using python that ses the FreeCurrencyAPI for live currency data.

## Usage
`currency_converter.py [amount] [start_currency] [end_currency]`

For example: `currency_converter.py 30 USD GBP` will convert $30 USD to GBP

For help use `currency_converter.py -h` 

To list all available currencies: `currency_converter.py --list-currencies`

### To Do:
1) Add some sort of support for matching based on name (ie new zealand is converted to NZD automatically
2) Create a UI
3) More error handling possibly

### Available Currency Abbreviations and Full Names
| Abbreviation | Full Name |
|---|---|
| EUR | Euro |
| USD | US Dollar |
| JPY | Japanese Yen |
| BGN | Bulgarian Lev |
| CZK | Czech Republic Koruna |
| DKK | Danish Krone |
| GBP | British Pound Sterling |
| HUF | Hungarian Forint |
| PLN | Polish Zloty |
| RON | Romanian Leu |
| SEK | Swedish Krona |
| CHF | Swiss Franc |
| ISK | Icelandic Króna |
| NOK | Norwegian Krone |
| HRK | Croatian Kuna |
| RUB | Russian Ruble |
| TRY | Turkish Lira |
| AUD | Australian Dollar |
| BRL | Brazilian Real |
| CAD | Canadian Dollar |
| CNY | Chinese Yuan |
| HKD | Hong Kong Dollar |
| IDR | Indonesian Rupiah |
| ILS | Israeli New Sheqel |
| INR | Indian Rupee |
| KRW | South Korean Won |
| MXN | Mexican Peso |
| MYR | Malaysian Ringgit |
| NZD | New Zealand Dollar |
| PHP | Philippine Peso |
| SGD | Singapore Dollar |
| THB | Thai Baht |
| ZAR | South African Rand |