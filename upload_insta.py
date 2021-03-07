import argparse
import os
from pathlib import Path

import instabot
import requests
from dotenv import load_dotenv
from PIL import Image


def create_parser():
    load_dotenv()

    images_path = os.getenv('IMAGES_DIRECTORY')

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Путь до изображений для отправки', default=images_path)
    return parser


def download_images(image_name, image_link, directory):
    Path(directory).mkdir(parents=True, exist_ok=True)

    response = requests.get(image_link, verify=False)
    response.raise_for_status()

    with open(f'{directory}/{image_name}', mode='wb') as pic:
        pic.write(response.content)


def format_image(link_images):
    slice_link = link_images.split('/')[-1]
    return slice_link.split('.')[-1]


def resize_photo(directory):
    for file in os.listdir(directory):
        imag = Image.open(f'{directory}/{file}')
        imag.thumbnail((1080, 1080))
        imag.save(f'{directory}/{file}', format="JPEG")


def upload_instagram():
    load_dotenv()
    insta_username = os.getenv('INSTAGRAM_USERNAME')
    insta_password = os.getenv('INSTAGRAM_PASSWORD')

    parser = create_parser()
    args = parser.parse_args()
    images_path = args.path

    resize_photo(images_path)

    bot = instabot.Bot()
    bot.login(username=insta_username, password=insta_password)

    insta_images_names = os.listdir(images_path)
    for insta_image_name in insta_images_names:
        bot.upload_photo(f'{images_path}/{insta_image_name}')


if __name__ == '__main__':
    upload_instagram()