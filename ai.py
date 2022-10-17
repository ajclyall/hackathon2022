#import replicate
#import requests
#from os.path import exists

#rep = replicate.Client(api_token="7e406bcd99e5fd119d2ca85e19a038ab6d890d05")
#model = rep.models.get("stability-ai/stable-diffusion")


#def generate_image(image_state):
    #prompt = image_state.content[0]
    #file_name = image_state.id
    #if not exists(f'images/{file_name}.png'):
     #   data = requests.get(model.predict(prompt=prompt)[0]).content
      #  with open(f"images/{file_name}.png", "wb") as file:
       #     file.write(data)
