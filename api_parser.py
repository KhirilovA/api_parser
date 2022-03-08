import requests

def api_parse(url:str):
    try:
        return requests.get(url, timeout=5).json()
    except requests.exceptions.ConnectionError:
        return "Error Connecting: Connection Error occured"
    except requests.exceptions.Timeout:
        return "Timeout Error: Timeout Error occured"
