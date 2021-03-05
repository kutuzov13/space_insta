import os

import requests


def get_images_spacex():
    api_spacex = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(api_spacex)
    response.raise_for_status()
    images_spacex = response.json()['links']['flickr']['original']
    return images_spacex


def download_images(image_name, link_image):
    directory = './images'
    response = requests.get(link_image)
    response.raise_for_status()
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f'{directory}/{image_name}.jpeg', mode='wb') as pic:
        pic.write(response.content)


for image_number, image in enumerate(get_images_spacex()):
    download_images(image_number, image)