import os
from urllib.parse import urlparse, unquote

import requests


def download_image(image_name, image_link, directory):

    response = requests.get(image_link, verify=False)
    response.raise_for_status()

    with open(f'{directory}/{image_name}', mode='wb') as pic:
        pic.write(response.content)


def get_file_extension(link_images):
    parsed_link = urlparse(link_images)
    return os.path.splitext(unquote(parsed_link.path))[-1]