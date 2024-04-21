import unittest
import requests
from yandex_API import access_token_ya

class TestYandexDiskAPI(unittest.TestCase):

    def setUp(self):
        self.access_token_ya = access_token_ya
        self.path = 'New_folder'
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Authorization': 'OAuth ' + self.access_token_ya}

    def test_create_folder_success(self):
        params = {'path': self.path}
        response = requests.put(self.url, params=params, headers=self.headers)
        self.assertIn(response.status_code, [200, 201, 202])
        self.assertTrue(response.json().get('href') is not None)


    def test_invalid_path(self):
        params = {'path': 'invalid_path'}
        response = requests.put(self.url, params=params, headers=self.headers)
        self.assertNotIn(response.status_code, [200, 201, 202])


if __name__ == '__main__':
    unittest.main()