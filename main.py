import replicate

model = replicate.models.get("stability-ai/stable-diffusion")
output = model.predict(prompt="little goblin man")
print(output)

