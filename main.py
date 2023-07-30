import requests


# Задача номер 3

supers = ['Hulk', 'Captain America', 'Thanos']

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
resp = requests.get(url, params=None)
resp_1 = resp.json()

count = []
names = []

heroes = [
    super_hero for super_hero in resp_1 if super_hero['name'] in supers
]

for bits in heroes:
    names.append(bits['name'])
    count.append(bits['powerstats']['intelligence'])

d = dict(zip(count, names))
print(max(d.values()))


# Задача номер 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = {'Authorization': 'OAuth ' +self.token}
        params = {'path': '/Netologiya.png'}
        data = requests.get(url, headers=headers, params=params).json()
        url = data['href']
        with open(file_path, 'rb') as f:
            response = requests.put(url, files={'file': f}, headers=headers, params=params)
        return response.status_code

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:\\Users\\Денис\\Desktop\\Homework\\Netologiya-0.png"
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
