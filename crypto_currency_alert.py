# We are going to create cryptocurrency alert.
# API:https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD
# vs_currency=USD - Can be changed
import requests;
from dataclasses import dataclass;
from typing import Final;
baseurl: Final[str]="https://api.coingecko.com/api/v3/coins/markets"; # Final means it cannot be modified

def alert(current_price):
    if current_price > 25000:
        print("Price Alert Triggered. Value is more than 25000$");


def get_coins(coin_symbol):
    payload: dict = {'vs_currency': 'usd','order':'market_cap_desc'};
    data = requests.get(baseurl,params=payload);
    data = data.json();
    coin_list = ['name','symbol','current_price','high_24h','low_24h','price_change_24h','price_change_percentage_24h'];
    for i in data:
        if i.get('name').lower() == coin_symbol.lower():
            print(f'Name: ',coin_symbol);
            print(f'Current Price:', i.get('current_price'),'$');
            alert(i.get('current_price'));
            break;
        else:
            print(f'Coin {coin_symbol} Not Found...')
            break;

if __name__ == '__main__':
    coin_symbol: str = input(f'Enter Coin Name (Eg: Bitcoin): ');
    get_coins(coin_symbol);
