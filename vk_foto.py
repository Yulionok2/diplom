from pprint import pprint

import requests

_id_ = 'xxx'
Token = 'xxx' #токен для яндекс.диска
TOKEN = 'xxx' #токен для вк


class VKPhoto:
    def __init__(self, id_, token):
        self.id = id_
        self.token = token
        self.likes = {}

    def get_headers(self):
        return{
                'Content - Type': 'application/json',
                'Authorization': 'OAuth{}'.format(self.token)
            }

    def list_photo(self, extended=1):
        """
        Параметры album_id:
        wall — фотографии со стены;
        profile — фотографии профиля;
        saved — сохраненные фотографии. Возвращается только с ключом доступа пользователя.
        """
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id,
                  'access_token': TOKEN,
                  'v': '5.131',
                  'album_id': 'profile',
                  'extended': extended,
                  'count': 30}
        res = requests.get(url, params=params)
        return pprint(res.json())

    def likes_photo(self):
        res = self.list_photo()['response']['items']['likes']['count']
        self.likes['file_name'] = [res]

    # def size_photo(self):
    #     res = self.list_photo()['response']['items']['sizes'][10]
    #     return res

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()


if __name__ == '__main__':
    apivk = VKPhoto(_id_, Token)
    apivk.list_photo()