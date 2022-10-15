import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
gpt2 = GPT2LMHeadModel.from_pretrained('gpt2')


tokenizer.padding_side = "left"
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained('gpt2')
'''sequence = ("Hi my name is James "
            "I know you inherited the castle "
            "Have you heard the infinite horror stories about the bloody bicount "
            "He massacred hundreds of towns people "
            "He used to live in the castle on the hill "
            "We are all afraid "
            "The castle is haunted ")'''

sequence = ("Hi my name is James "
            "I know you inherited the castle "
            "Have you heard the infinite horror stories about the bloody viscount "
            "He used to live in the castle on the hill, "
            "and he massacred hundreds of towns people "
            )
inputs = tokenizer.encode(sequence, return_tensors='pt', padding=True)
outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=0.5)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)


# sentences = ["Hi, my name is James, and I heard you inherited the castle",
#              "Have you heard the story about the bloody viscount?",
#              "He murdered"]
# inputs = tokenizer(sentences, return_tensors="pt", padding=True)
#
# output_sequences = gpt2.generate(**inputs)
#
# for seq in output_sequences:
#     print(tokenizer.decode(seq))


from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
#print(generator("Hello Emma, I'm your text generator,", max_length=30, num_return_sequences=5))

#let us try something else please




#Scene 1: Phone call
CharName = "Emma" #temp
x = CharName
caller = generator("Hello " + x + ", this is Franchesco, I heard many terrible stories about the castle you are living in ", max_length=40, num_return_sequences=5)
#print(caller)


from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
text = ("Hi my name is James "
            "I know you inherited the castle "
            "Have you heard the infinite horror stories about the bloody bicount "
            "He used to live in the castle on the hill, "
            "and he massacred hundreds of towns people "
            )
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
textOut = tokenizer.decode(output[0], skip_special_tokens=True)
print(textOut)






#WE ARE TRYNG SOMETHING ELSE#

