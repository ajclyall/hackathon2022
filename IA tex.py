#this is just an example but it is working

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
print(generator("Hello Emma, I'm your text generator,", max_length=30, num_return_sequences=5))
