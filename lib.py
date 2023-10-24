from requests import Session
import json
import pprint
import requests


def get_price(api):  # Function to get the info

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"  # Coinmarketcap API url

    parameters = {
        "slug": "bitcoin",
        "convert": "USD",
    }  # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api,
    }  # Headers for the API request

    session = Session()  # Create new session object to manage API requests
    session.headers.update(
        headers
    )  # Update the session headers with the specified headers

    response = session.get(
        url, params=parameters
    )  # Receiving the response from the API

    info = json.loads(response.text)
    price = info["data"]["1"]["quote"]["USD"]["price"]
    # Extracting the price from the JSON data
    return price


def get_utxo(address):
    response = requests.get(f"https://mempool.space/api/address/{address}/utxo")
    data = response.json()
    utxos = data
    return sum([utxo["value"] for utxo in utxos]) / 10 ** 8  # 转换为比特币


def read_addr(path):
    with open(path, "r") as f:
        addrs = json.load(f)
    return addrs


def get_total_btc(addrs):
    total = 0
    for addr in addrs:
        total += get_utxo(addr)
    return total

def read_api(path):
    with open(path, "r") as f:
        api = json.load(f)
    return api[0]

def example(): 
    addrs = read_addr("address.json")
    btc = get_total_btc(addrs)
    api = read_api("api.json")
    price = get_price(api)
    print(f"BTC: {btc}, Price: {price}, Total: {btc * price}")