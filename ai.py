import replicate
import requests
from django.utils.text import slugify

rep = replicate.Client(api_token="3aad027667c111e232e6bc91732851bedede6b70")
model = rep.models.get("stability-ai/stable-diffusion")


def generate_image(prompt):

    data = requests.get(model.predict(prompt=prompt)[0]).content
    with open(f"{slugify(prompt)}.png", "wb") as file:
        file.write(data)

# def display_image():
#     # this whole file is unfinished, please be nice :)
#     data = requests.get(generate_image()[0])


# with open("test.png", 'wb') as file:
#     file.write(data.content)
