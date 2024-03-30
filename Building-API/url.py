import requests

parms ={
    "name": 'Good'
}

print(requests.get("krooz",params=parms))
