from flask import Flask, request, jsonify
from currency_converter import convert_currency, COUNTRY_TO_CURRENCY

app = Flask(__name__)

@app.route("/convert", methods=["POST"])
def conversion():
    data = request.json
    converted_amount = convert_currency(data["amount"], data["start_currency"], data["end_currency"], COUNTRY_TO_CURRENCY)
    response_message = f"{data['amount']} {data['start_currency']} is equal to {converted_amount} {data['end_currency']}"
    return jsonify({"message": response_message})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)