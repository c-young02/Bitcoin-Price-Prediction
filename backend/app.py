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
    
    print(f'This is the response from rapid api \n {r}')
    
    value = r["fgi"]["now"]["value"]
    
    print(f'This is the current fear and greed index value: {value}')
    
    response = jsonify(value)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)