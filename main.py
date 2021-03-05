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
    return print(slice_link.split('.')[-1])


hub = requests.get('http://hubblesite.org/api/v3/image/1', verify=True)
for i in hub.json()['image_files']:
    format_image(i["file_url"])


# if __name__ == '__main__':
#     fetch_spacex_last_launch()