import requests

def get_plants():
    response = requests.get('https://trefle.io/api/v1/plants') # Need token?