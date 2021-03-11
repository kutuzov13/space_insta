import argparse
import os
from pathlib import Path

import instabot
from dotenv import load_dotenv
from PIL import Image


MAX_SIZE = (1080, 1080)


def create_parser():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to images to send', default=os.getenv('IMAGES_PATH'))
    return parser


def resize_photos(directory):
    for file in os.listdir(directory):
        imag = Image.open(f'{directory}/{file}')
        imag.thumbnail(MAX_SIZE)
        imag.save(f'{directory}/{file}', format="JPEG")


def upload_instagram():
    load_dotenv()
    insta_username = os.getenv('INSTAGRAM_USERNAME')
    insta_password = os.getenv('INSTAGRAM_PASSWORD')

    parser = create_parser()
    args = parser.parse_args()
    images_path = args.path

    Path(images_path).mkdir(parents=True, exist_ok=True)

    resize_photos(images_path)

    bot = instabot.Bot()
    bot.login(username=insta_username, password=insta_password)

    insta_images_names = os.listdir(images_path)
    try:
        for insta_image_name in insta_images_names:
            bot.upload_photo(f'{images_path}/{insta_image_name}')
    except Exception as error:
        print(error)
        print('Photos are not fully uploaded. Try again')


if __name__ == '__main__':
    upload_instagram()