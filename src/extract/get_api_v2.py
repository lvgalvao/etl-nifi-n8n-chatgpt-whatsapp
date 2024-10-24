import requests
from pydantic import BaseModel

class bitcoin_price(BaseModel):
    amount: float   
    base: str
    currency: str

def get_bitcoin_price_pydantic():
    """Obtém o preço atual do Bitcoin na Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    response = requests.get(url)
    data = response.json().get("data")
    return bitcoin_price(**data)

# def get_bitcoin_price():
#     """Obtém o preço atual do Bitcoin na Coinbase."""
#     url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
#     response = requests.get(url)
#     print(response)
#     data = response.json()
#     print(data)
#     return 

if __name__ == "__main__":
    print(get_bitcoin_price_pydantic().amount)
