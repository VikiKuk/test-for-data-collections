import requests

class YANDEX:

    def __init__(self, access_token_ya, path):
        self.token = 'OAuth ' + access_token_ya
        self.headers = {'Authorization': self.token}
        self.path = path

    def create_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.path}
        response = requests.put(url, params=params, headers=self.headers)
        errors = []
        if response.status_code in [200, 201, 202, 409]:
            print('--------')
            print('Папка для фото успешно создана.')
        else:
            print(response)
            errors.append(response.json()['message'])
        if len(errors) != 0:
            print()
            print('--------')
            print('При создании папки возникли проблемы. Перечень ошибок:')
            for item in errors:
                print(item)

access_token_ya = 'input_your token'
