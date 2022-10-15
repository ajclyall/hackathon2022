
from PIL import ImageTk, Image

import replicate
import requests

import gui

rep = replicate.Client(api_token="3aad027667c111e232e6bc91732851bedede6b70")
model = rep.models.get("stability-ai/stable-diffusion")

def generate_image(prompt):
    return model.predict(prompt=prompt)

def display_image():
    # this whole file is unfinished, please be nice :)
    data = requests.get(generate_image()[0])


# with open("test.png", 'wb') as file:
#     file.write(data.content)



