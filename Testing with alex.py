
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#gpt2 = GPT2LMHeadModel.from_pretrained('gpt2')


#tokenizer.padding_side = "left"
#tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained('gpt2')

sequence = ("Hi my name is James \n"
            "I know you inherited the castle \n"
            "Have you heard the infinite horror stories about the bloody viscount \n"
            "He used to live in the castle on the hill, \n"
            "and he massacred hundreds of towns people \n"
            )
inputs = tokenizer.encode(sequence, return_tensors='pt')
outputs = model.generate(inputs, max_length=150, do_sample=True, temperature=0.5, top_k=50, no_repeat_ngram_size=2, early_stopping=True)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)


points = ['!', '?', '.']
text = text.replace(u'\xa0', u' ')
textArray = text.split('\n')

if(textArray[-1].rstrip()[-1] not in points):
    textArray = textArray[0:-1]

for i in range(len(textArray)):
    print(textArray[i])

