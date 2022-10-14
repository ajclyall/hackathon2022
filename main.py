import replicate
rep = replicate.Client(api_token="3aad027667c111e232e6bc91732851bedede6b70")
model = rep.models.get("stability-ai/stable-diffusion")
output = model.predict(prompt="little goblin man")
print(output)

