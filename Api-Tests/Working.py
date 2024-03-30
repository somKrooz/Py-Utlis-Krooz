import asyncio
import aiohttp

url = 'https://api.waifu.im/search'

params = {
    'included_tags': ['maid'],
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
            with open(filename, 'wb') as f:
                f.write(image_data)
        else:
            print(f"Failed to download image from {url}, status code: {response.status}")

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        myImg = []
        responses = await asyncio.gather(*tasks)
        for idx, response in enumerate(responses):
            if idx % 2 == 0:  # Skipping sleep tasks
                try:
                    data = await response.json()
                    new = data['images'][0]['url']
                    name = str(new).split('/')[-1]
                    myImg.append(download_image(session, new, f"Krooz/{name}"))
                except Exception as e:
                    print(f"Error: {e}")
        await asyncio.gather(*myImg)

asyncio.run(get_symbols())
