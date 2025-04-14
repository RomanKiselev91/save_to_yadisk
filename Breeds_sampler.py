import requests
import random
from requests import get, ConnectionError
from requests_oauthlib import OAuth2Session
from requests import get, post, put, delete

'''информация о состоянии облачного хранилища'''
TOKEN = 'y0__xC08su4BhjblgMg0cj24BJE4l5nQiqWXb8TVb-ViZH8oMP5Aw'
headers = {"Authorization": f"OAuth {TOKEN}"}
r_disk = get("https://cloud-api.yandex.net/v1/disk", headers=headers)

'''создаю папку'''
params = {"path": "Breeds"}
r_disk = put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)

response= requests.get('https://dog.ceo/api/breeds/list/all')
response_json=response.json()

for breed, subbreeds  in response_json['message'].items():
    for subbreed in subbreeds:
        if len(subbreed) >=10:

            r = requests.get(f'https://dog.ceo/api/breed/{breed}/{subbreed}/images/random')
            response_json = r.json()

            r = requests.get(response_json['message'])
            name = f'{breed} {subbreed}' + '.jpg'

            with open(name, 'wb') as file:
                file.write(r.content)

            params = {"path": f"Breeds/{name}"}
            r_disk = get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                    headers=headers, params=params)
            href = r_disk.json()["href"]

            files = {"file": open(f"{name}", "rb")}
            r_disk = put(href, files=files)