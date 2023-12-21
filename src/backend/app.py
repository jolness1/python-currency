from flask import Flask, request, jsonify
from currency_converter import convert_currency, COUNTRY_TO_CURRENCY, CURRENCY_SYMBOLS

app = Flask(__name__)


@app.route("/convert", methods=["POST"])
def conversion():
    data = request.json
    conversion_result = convert_currency(data["amount"], data["start_currency"], data["end_currency"], COUNTRY_TO_CURRENCY)
    return jsonify({"message": conversion_result})


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=8000,
            # Disable debug later
            debug=True
            )
