import requests
from concurrent.futures import ThreadPoolExecutor
import random
import time

session = requests.Session()
def getRandomHeader():
    Choices = ["wifu","maid","oppai","selfies","uniform",'marin-kitagawa',"mori-colliope"]
    val = random.choice(Choices)
    print(val)
    return val

urls = []
for i in range(5):
    urls.append('https://api.waifu.im/search')

def fetch_url(url):

    hdr = {
        'include_tags': 'maid',
        "Authorization":'IbbDSpAQ8xJuRM0zobKhDM9_CRfBPbC9K3L3F_gXBR6IpcF-ZGfuCdU2ITy1qDvfcMFr-7-X2ae5UcDiabtibSlC4ooRIujLX8XmO8CZW_LpY1hNz5AXax8kwlI8l2RRnNc2ClxpseIbi5xinaNT8JMjY61wFRMdgmvjOX4bRyk',
        'Accept-Version': 'v5',
        'Retry-After': '.3',
    }
    
    param = {
        
        # 'is_nsfw': 'true'
    }

    response = requests.get(url,headers=hdr,params=param)
    if response.status_code == 200:
        res = response.json()
        new = res['images'][0]['url']
        Name = res['images'][0]['signature'] 
        response = session.get(new, stream=True)
        with open(f"OUT/{Name}.jpg", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
    
    if response.status_code == 429 :
        print("Error 429 Data Queued")

def send_requests(urls):
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(fetch_url, urls))

    return results

results = send_requests(urls)   
time.sleep(2)
