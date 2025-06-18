import requests

access_token =
URL = "https://cloud-api.yandex.net/v1/disk/resources"
URL_UPLOAD = 'https://cloud-api.yandex.net/v1/disk/resources/upload?'
headers = {"Authorization": f"OAuth {access_token}"}
URL_image = 'https://cataas.com/cat/says/'

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)
    return path

def save_yadisk(folder, text):
    response = requests.post(URL_UPLOAD, headers=headers,
                                params={'path': f'{folder}/{text+'.jpg'}', 'url': f'{URL_image + text}'})

def save_loc(text):
    response = requests.get(URL_image + text)
    with open(text + '.jpg', 'wb') as file:
        file.write(response.content)
def start_prog():
    text = input('enter text')
    path_save = input('Куда сохранить?')

    if path_save == 'yadisk':
        folder = create_folder(text)
        yadisk = save_yadisk(folder, text)
        print('Сохранено на Ядиск')
    else:
        locdisk = save_loc(text)
        print('Сохранено на локальный диск')
start_prog()
