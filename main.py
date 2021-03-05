import os

import requests

image_name = 'sputnik.jpeg'
link_to_image = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
directory = './images'

response = requests.get(link_to_image)
response.raise_for_status()
if not os.path.exists(directory):
    os.makedirs(directory)
with open(f'{directory}/{image_name}', mode='wb') as image:
    image.write(response.content)