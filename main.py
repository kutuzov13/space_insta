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
    with open(f'{directory}/{image_name}.jpg', mode='wb') as pic:
        pic.write(response.content)


def fetch_spacex_last_launch():
    for image_names, image in enumerate(get_images_spacex()):
        download_images(f'spacex{image_names}', image)


def format_image(link_images):
    slice_link = link_images.split('/')[-1]
    return slice_link.split('.')[-1]


def download_images_hubble(image_id):
    api_hubble = 'http://hubblesite.org/api/v3/image/{}'
    response = requests.get(api_hubble.format(image_id))
    response.raise_for_status()
    for photo in response.json()['image_files']:
        response = requests.get(f'https:{photo["file_url"]}', verify=False)
        response.raise_for_status()
        with open(f'{image_id}.{format_image(photo["file_url"])}', mode='wb') as pic:
            pic.write(response.content)


if __name__ == '__main__':
    download_images_hubble('1')