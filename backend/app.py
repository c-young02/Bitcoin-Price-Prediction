from flask import Flask, jsonify
import requests
import os
import sys
import numpy as np

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Append the ml_model directory to the parent directory
sys.path.append(os.path.join(parent_dir, 'ml_model'))

from run import predict_bitcoin_price

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Backend is working!'


@app.route('/FearandGreed', methods=['GET'])
def fear_and_greed():
    
    headers = {
                'X-RapidAPI-Key': '4353b85175msh248aef35ff35de8p10ed5ajsnfd5b6d988cf0',
                'X-RapidAPI-Host': 'fear-and-greed-index.p.rapidapi.com'
            }
    
    r = requests.get("https://fear-and-greed-index.p.rapidapi.com/v1/fgi", headers=headers)
    
    r = r.json()
    
    value = r["fgi"]["now"]["value"]
    
    print(f'This is the current fear and greed index value: {value}')
    
    response = jsonify(value)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/CryptoInfo', methods=['GET'])
def cryptoInfo():
    
    headers = {
                'X-CMC_PRO_API_KEY': '1e826d4b-59a1-46c8-8ea5-49466cb4a0b7',
                'Accept': 'application/json'
            }
    
    r = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?&limit=1&convert=GBP", headers=headers)
    
    r = r.json()

    # Fetch the current USD to GBP exchange rate
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    usd_to_gbp = data['rates']['GBP']
    
    cmc_rank = r['data'][0]['cmc_rank']
    current_price = round(r['data'][0]['quote']['GBP']['price'], 2)
    
    market_cap = r['data'][0]['quote']['GBP']['market_cap']
    formatted_num = "{:,.2f}".format(market_cap)
    market_capList = formatted_num.split(',')
    market_cap = market_capList[0] + ',' + market_capList[1]
    
    market_dominance = round(r['data'][0]['quote']['GBP']['market_cap_dominance'], 2)
    market_dominance = str(market_dominance)+ '%'
    
    crypto_name = r['data'][0]['slug']
    
    circulating_supply = r['data'][0]['circulating_supply']
    formatted_supply = "{:,}".format(circulating_supply)
    circulating_supplyList = formatted_supply.split(',')
    circulating_supply = circulating_supplyList[0]
    # Define an array of model paths
    model_paths = ["../models/model_1.h5", "../models/model_7.h5", "../models/model_14.h5"]

    # Call the function to predict the bitcoin price
    predicted_prices = predict_bitcoin_price(model_paths)

    # Convert the predicted prices to GBP
    predicted_prices_gbp = [price * usd_to_gbp for price in predicted_prices]

    # Round the predicted prices to 2 decimal places
    predicted_prices_value = [np.round(price.item(), 2) for price in predicted_prices_gbp]
    
    print(cmc_rank)
    print(current_price)
    print(market_cap)
    print(market_dominance)
    print(crypto_name)
    print(circulating_supply)
    print(predicted_prices_value)

    response = jsonify({
        'rank': cmc_rank,
        'current_price': '£' + str(current_price),
        'market_cap': market_cap,
        'market_dominance': market_dominance,
        'crypto_name': crypto_name,
        'circulating_supply': str(circulating_supply) + 'M',
        'predicted_prices': ['£' + str(price) for price in predicted_prices_value]
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True)
