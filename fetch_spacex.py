import argparse
from pathlib import Path

import requests

from upload_insta import download_image, get_file_extension


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id запуска', default='latest')
    parser.add_argument('--download_path', help='Путь куда надо скачивать изображения', default='images')
    return parser


def fetch_image_spacex():
    parser = create_parser()
    args = parser.parse_args()
    spacex_launch_id = args.id
    spacex_path_images = args.download_path
    Path(spacex_path_images).mkdir(parents=True, exist_ok=True)
    api_spacex = f'https://api.spacexdata.com/v3/launches/{spacex_launch_id}/'

    response = requests.get(api_spacex)
    response.raise_for_status()

    images_spacex_url = response.json()['links']['flickr_images']
    for image_names, spacex_url in enumerate(images_spacex_url):
        spacex_filename = f'spacex{image_names}.{get_file_extension(spacex_url)}'
        download_image(spacex_filename, spacex_url, spacex_path_images)


if __name__ == '__main__':
    fetch_image_spacex()