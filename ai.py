import replicate
import requests


rep = replicate.Client(api_token="e53c3e92e92cedf6f1e24a377e261efa92d83a0d")
model = rep.models.get("stability-ai/stable-diffusion")


def generate_image(image_state):
    prompt = image_state.content[0]
    file_name = image_state.id
    data = requests.get(model.predict(prompt=prompt)[0]).content
    with open(f"images/{file_name}.png", "wb") as file:
        file.write(data)
