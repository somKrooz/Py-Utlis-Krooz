import requests
import random

session = requests.Session()

url = 'https://api.waifu.im/search'

params = {
    'included_tags': ['maid'],
    'height': '>=2000',
    'Accept-Version': 'v5'
}

res = session.get(url, params=params)

# why is this too damn slow
if res.status_code == 200:
    data = res.json()
    new = data['images'][0]['url']
    print(new)