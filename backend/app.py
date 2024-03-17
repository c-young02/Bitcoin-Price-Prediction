from flask import Flask, request, jsonify
import requests

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
    
    cmc_rank = r['data'][0]['cmc_rank']
    current_price = round(r['data'][0]['quote']['GBP']['price'], 2)
    predicted_price = 0
    
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
    
    print(cmc_rank)
    print(current_price)
    print(market_cap)
    print(market_dominance)
    print(crypto_name)
    print(circulating_supply)
    
    response = jsonify({
        'rank': cmc_rank,
        'current_price': current_price,
        'market_cap': market_cap,
        'market_dominance': market_dominance,
        'crypto_name': crypto_name,
        'circulating_supply': circulating_supply
        })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)