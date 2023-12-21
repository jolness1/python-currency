# Currency Converter

A simple script for converting currencies using python that ses the FreeCurrencyAPI for live currency data.

## Usage
### Starting the Backend
1) Navigate to the `backend` directory
2) `python3 app.py` - app will run on port 8000 by default

#### Starting the Frontend
*TODO*

#### Use standalone
`python2 currency_converter.py` and follow prompts
*or*
`python3 currency_converter.py [amount] [start_currency] [end_currency]`

For example: `currency_converter.py 30 USD GBP` will convert $30 USD to GBP

Also supports using country name ie `germany`

Is not case-sensitive, `usd` is treated the same as `USD` 

For help use `currency_converter.py -h` 

To list all available currencies: `currency_converter.py --list-currencies`

### To Do:
1) Create a Frontend
2) Add ability to list all country names

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

### Available Countries and their respective currency abbreviations
| Country           | Currency Code |
|-------------------|---------------|
| Australia         | AUD           |
| Austria           | EUR           |
| Belgium           | EUR           |
| Brazil            | BRL           |
| Bulgaria          | BGN           |
| Canada            | CAD           |
| China             | CNY           |
| Croatia           | EUR           |
| Cyprus            | EUR           |
| Czech Republic    | CZK           |
| Denmark           | DKK           |
| Estonia           | EUR           |
| Finland           | EUR           |
| France            | EUR           |
| Germany           | EUR           |
| Greece            | EUR           |
| Hong Kong         | HKD           |
| Hungary           | HUF           |
| Iceland           | ISK           |
| India             | INR           |
| Indonesia         | IDR           |
| Ireland           | EUR           |
| Israel            | ILS           |
| Italy             | EUR           |
| Japan             | JPY           |
| Latvia            | EUR           |
| Lithuania        | EUR           |
| Luxembourg        | EUR           |
| Malaysia          | MYR           |
| Malta             | EUR           |
| Mexico            | MXN           |
| Netherlands       | EUR           |
| New Zealand       | NZD           |
| Norway            | NOK           |
| Philippines       | PHP           |
| Poland            | PLN           |
| Portugal          | EUR           |
| Romania           | RON           |
| Russia            | RUB           |
| Singapore         | SGD           |
| Slovakia          | EUR           |
| Slovenia          | EUR           |
| South Africa      | ZAR           |
| South Korea       | KRW           |
| Spain             | EUR           |
| Sweden            | SEK           |
| Switzerland       | CHF           |
| Thailand          | THB           |
| Turkey            | TRY           |
| United Kingdom    | GBP           |
| United States     | USD           |
