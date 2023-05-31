from django.shortcuts import render

import requests
import json

def bitcoin_price(request):
    response = requests.get('https://api.cryptoapis.io/v1/bc/btc/mainnet/info')
    data = json.loads(response.text)
    bitcoin_price = data['data']['last_block']['price']
    return render(request, 'bitcoin_price.html', {'bitcoin_price': bitcoin_price})

