import argparse
from pathlib import Path

import requests

from upload_insta import download_image, get_file_extension


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id запуска')
    parser.add_argument('--download_path', help='Путь куда надо скачать изображения', default='images')
    return parser


def fetch_image_hubble():
    parser = create_parser()
    args = parser.parse_args()
    hubble_launch_id = args.id
    hubble_path_images = args.download_path
    Path(hubble_path_images).mkdir(parents=True, exist_ok=True)
    api_hubble = f'http://hubblesite.org/api/v3/image/{hubble_launch_id}'

    response = requests.get(api_hubble)
    response.raise_for_status()

    last_image_hubble = response.json()['image_files'][-1]
    last_image_url = f'https:{last_image_hubble["file_url"]}'
    hubble_filename = f'hubble{hubble_launch_id}.{get_file_extension(last_image_hubble["file_url"])}'
    download_image(hubble_filename, last_image_url, hubble_path_images)


if __name__ == '__main__':
    fetch_image_hubble()