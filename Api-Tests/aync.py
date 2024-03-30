import asyncio
import aiohttp
import random


url = 'https://api.waifu.im/search'

def getRandomHeader():
    Choices = ["wifu","maid","oppai","selfies","uniform"]
    val =  random.choice(Choices)
    print(val)
    return val
params = {
    'included_tags': getRandomHeader(),
    'height': '>=2000'
    
}

def get_tasks(session):
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(session.get(url, params=params, ssl=False)))
        tasks.append(asyncio.sleep(0.3)) 
    return tasks

async def download_image(session, url, filename):
    async with session.get(url) as response:
        if response.status == 200:
            image_data = await response.read()
            # Save the image data to a file
            with open(filename, 'wb') as f:
                f.write(image_data)

async def get_symbols():
     async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        myImg = []
        responses = await asyncio.gather(*tasks)
        for idx, response in enumerate(responses):
            if idx % 2 == 0:  
                data = await response.json()
                new = data['images'][0]['url']
                name = str(new).split('/')[-1]
                myImg.append(download_image(session, new, f"Krooz/{name}"))
        await asyncio.gather(*myImg)

asyncio.run(get_symbols())