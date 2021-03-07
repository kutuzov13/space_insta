import os

import instabot
import requests
from dotenv import load_dotenv
from PIL import Image


def fetch_image_spacex():
    api_spacex = 'https://api.spacexdata.com/v4/launches/latest'

    response = requests.get(api_spacex)
    response.raise_for_status()
    images_spacex = response.json()['links']['flickr']['original']
    for image_names, image in enumerate(images_spacex):
        download_images(f'spacex{image_names}', f'{image}')


def download_images(image_name, link_image):
    directory = './images'
    response = requests.get(link_image, verify=False)
    response.raise_for_status()
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f'{directory}/{image_name}.jpg', mode='wb') as pic:
        pic.write(response.content)


def format_image(link_images):
    slice_link = link_images.split('/')[-1]
    return slice_link.split('.')[-1]


def fetch_image_hubble(image_id):
    api_hubble = f'http://hubblesite.org/api/v3/image/{image_id}'

    response = requests.get(api_hubble)
    response.raise_for_status()

    last_image = response.json()['image_files'][-1]
    last_image_url = f'https:{last_image["file_url"]}'
    file_name = f'hubble{image_id}.{format_image(last_image["file_url"])}'
    download_images(file_name, last_image_url)


def resize_photo():
    directory = './images/'
    for file in os.listdir(directory):
        imag = Image.open(f'{directory}/{file}')
        imag.thumbnail((1080, 1080))
        imag.save(f'{directory}/{file}', format="JPEG")


def upload_instagram():
    load_dotenv()
    insta_username = os.getenv('INSTAGRAM_USERNAME')
    insta_password = os.getenv('INSTAGRAM_PASSWORD')

    directory = './images'
    resize_photo()
    bot = instabot.Bot()
    bot.login(username=insta_username, password=insta_password)

    insta_images_names = os.listdir(directory)
    for insta_image_name in insta_images_names:
        bot.upload_photo(f'{directory}/{insta_image_name}')


if __name__ == '__main__':
    fetch_image_spacex()