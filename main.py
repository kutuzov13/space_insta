import os

import requests


directory = './images'


def download_images(link_image, image_name):
    response = requests.get(link_image)
    response.raise_for_status()
    if not os.path.exists(directory):
        os.makedirs(directory)
        with open(f'{directory}/{image_name}', mode='wb') as image:
            image.write(response.content)


name = 'sputnik.jpeg'
link_to_image = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
download_images(link_to_image, name)