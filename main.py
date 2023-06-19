import os
import json
import VkDownloader
import yadisk


vk_token = 'vk1.a.9WKlCdKB4SyHsvZVWFJJQBjr7g7yiRR6H6dX7ahToF0ie-V1pOLvptCZGtRrl2wESwywtqqPa6jljay47Zu0y9jveoCJ2L9ZDQgtI-sLMr98MOaxjiOnAcUN7pz6IllQ7lbgVlysfe4b5IMSZUl2kW-Ban-lo65ZTl2yoD_NfHLUlWm7GgO5h4D5xAcdTGk5yx-hI9cYSUAI8Z2X8i6JBg'
ya_token = 'y0_AgAAAAAe8BS-AADLWwAAAADimc0xjUliX3ljTB-FlWyvZkC1a9K9ZWw'

y = yadisk.YaDisk(token=ya_token)
downloader = VkDownloader.VkDownload(vk_token)
downloader.get_all_photos()

data = downloader.get_photos()
def get_json(data):
    max_size_photo = {}
    photos = []
    for photo in data['response']['items']:
        max_size = 0
        photos_info = {}
        
        for size in photo['sizes']:
            if size['height'] >= max_size:
                max_size = size['height']
        if photo['likes']['count'] in max_size_photo:
            photos_info['file_name'] = f"{photo['likes']['count']}+{photo['date']}.jpg"
        else:
            photos_info['file_name'] = f"{photo['likes']['count']}.jpg"
        photos_info['size'] = size['type']
        photos.append(photos_info)

    with open("photos.json", "w") as file:
        json.dump(photos, file, indent=4)

get_json(data)

photos_list = os.listdir('images_vk')
if not y.exists('photo'):
    y.mkdir('photo')
for count, photo_name in enumerate(photos_list, start=1):
    y.upload(f'images_vk/{photo_name}', '/photo/'f'{photo_name}')
    print(f'Загружено фото: {count}')