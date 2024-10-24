import requests

def get_bitcoin_price():
    """Obtém o preço atual do Bitcoin na Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    response = requests.get(url)
    data = response.json()
    price = data['data']['amount']
    print(f"Preço atual do Bitcoin: ${price} USD")
    return float(price)

if __name__ == "__main__":
    get_bitcoin_price()
