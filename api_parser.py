import requests

def api_parse(url:str='https://jsonplaceholder.typicode.com/users/1'):
    try:
        return requests.get(url).json()
    except requests.exceptions.ConnectionError as ConnectionError:
        raise ConnectionError 
    except requests.exceptions.Timeout as Timeout:
        raise Timeout
