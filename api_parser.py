import requests

def api_parse(url:str):
    return requests.get(url).json()
    