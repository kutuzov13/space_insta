import requests

image_name = 'sputnik.jpeg'
link_to_image = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

response = requests.get(link_to_image)
response.raise_for_status()

with open(image_name, mode='wb') as image:
    image.write(response.content)