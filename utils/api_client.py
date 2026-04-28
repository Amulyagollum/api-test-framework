import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint):
    
    return ( requests.get(f"{BASE_URL}/{endpoint}"))
   








    