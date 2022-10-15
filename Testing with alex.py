import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
gpt2 = GPT2LMHeadModel.from_pretrained('gpt2')


tokenizer.padding_side = "left"
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained('gpt2')

sequence = ("Hi my name is James "
            "I know you inherited the castle "
            "Have you heard the infinite horror stories about the bloody viscount "
            "He used to live in the castle on the hill, "
            "and he massacred hundreds of towns people "
            )
inputs = tokenizer.encode(sequence, return_tensors='pt', padding=True)
outputs = model.generate(inputs, max_length=100, do_sample=True, temperature=1, top_k=50)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)