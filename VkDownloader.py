import os
import requests

NAME = 'VkDownloader'

vk_token = 'vk1.a.9WKlCdKB4SyHsvZVWFJJQBjr7g7yiRR6H6dX7ahToF0ie-V1pOLvptCZGtRrl2wESwywtqqPa6jljay47Zu0y9jveoCJ2L9ZDQgtI-sLMr98MOaxjiOnAcUN7pz6IllQ7lbgVlysfe4b5IMSZUl2kW-Ban-lo65ZTl2yoD_NfHLUlWm7GgO5h4D5xAcdTGk5yx-hI9cYSUAI8Z2X8i6JBg'
user_id = str(input('Введите id пользователя VK: '))

class VkDownload:
    
    def __init__(self, token):
        self.token = token
            
    def get_photos(self, offset=0, count=50):

        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': user_id,
                    'album_id': 'profile',
                    'access_token': vk_token,
                    'v': '5.131',
                    'extended': '1',
                    'photo_sizes': '1',
                    'count': count,
                    'offset': offset
                    }
        res = requests.get(url=url, params=params)
        try:
            r = requests.get(url)
            if r.status_code != 200:
                print('Ошибка:')
                print(r.status_code)
        except Exception:
            print('Не опознанная ошибка')
        return res.json()
    
    def get_all_photos(self):
        data = self.get_photos()
        all_photo_count = data['response']['count']
        i = 0
        count = 50
        max_size_photo = {}
        

        if not os.path.exists('images_vk'):
            os.mkdir('images_vk')

        while i <= all_photo_count:
            if i != 0:
                data = self.get_photos(offset=i, count=count)


            for photo in data['response']['items']:
                max_size = 0
                

                for size in photo['sizes']:
                    if size['height'] >= max_size:
                        max_size = size['height']
                if photo['likes']['count'] in max_size_photo:
                    max_size_photo[f"{photo['likes']['count']} + {photo['date']}"] = size['url']

                else:
                    max_size_photo[photo['likes']['count']] = size['url']
                
            for photo_name, photo_url in max_size_photo.items():
                with open(f'images_vk/{photo_name}.jpg', 'wb') as file:
                    img = requests.get(photo_url)
                    file.write(img.content)
                    
            print(f'Загружено {len(max_size_photo)} фото')
            i += count
        
        
        


        

        

