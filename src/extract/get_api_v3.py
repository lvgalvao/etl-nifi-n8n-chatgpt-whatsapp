import requests
from src.extract.models.bitcoin_price_model import BitcoinPrice

def get_bitcoin_price():
    """Obtém o preço atual do Bitcoin na Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    response = requests.get(url)
    data = response.json().get("data")
    return BitcoinPrice(
        amount=float(data["amount"]),
        base=data["base"],
        currency=data["currency"]
    )
