import requests 

def download_image(url, filename):
    session = requests.Session()
    response = session.get(url)
    if response.status_code == 200:
        with open(str(filename), 'wb') as file:
            file.write(response.content)
        print(f"{filename} Done.")
    else:
        print(f"{response.status_code} Failed.")

def Name(name):
    split = str(name).split('/')
    print(split[-1])
    return split[-1]

image_url = "https://static.fandomspot.com/images/03/12657/04-misaki-ayuzawa-maid-sama-anime.jpg"
download_image(image_url, Name(image_url))



