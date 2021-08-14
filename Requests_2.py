import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        if os.path.exists(file_path):
            name = os.path.basename(file_path)
            try:
                get_url = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={name}'
                post_url = requests.get(get_url, headers={'Authorization': self.token}).json()['href']
            except KeyError:
                return f'Файл с именем "{name}" уже существует и не будет загружен!'
            else:
                with open(file_path, 'rb') as file:
                    requests.put(post_url, data=file)
                    return f'Файл с именем "{name}" успешно загружен!'
        else:
            return 'Загружаемый файл не найден на диске!'


path_to_file = ''
ya_token = ''

uploader = YaUploader(ya_token)
result = uploader.upload(path_to_file)
print(result)
