import urllib

import replicate
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen, Request
import requests


rep = replicate.Client(api_token="3aad027667c111e232e6bc91732851bedede6b70")
model = rep.models.get("stability-ai/stable-diffusion")

output = model.predict(prompt="cupcakes")


# def display_image(image_url):
#     # request_site = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
#
#     req = Request(
#         url=image_url,
#         headers={'User-Agent': 'Mozilla/5.0'}
#     )
#
#     webpage = urlopen(req).read()
#     root = tk.Tk()
#     u = urlopen(image_url)
#     raw_data = u.read()
#     u.close()
#
#     photo = ImageTk.PhotoImage(data=raw_data)
#     label = tk.Label(image=photo)
#     label.image = photo
#     label.pack()
#
#     root.mainloop()

