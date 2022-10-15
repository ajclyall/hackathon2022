
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from ConvStarters import caller,townMan

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')


#THINGS THAT WILL CHANGE IN EACH CASE

#input text
#length of answer
max_length = 150



#Towns man 1
sequence = ("Hi my name is James \n"
            "I know you inherited the castle \n"
            "Have you heard the infinite horror stories about the bloody viscount \n"
            "He used to live in the castle on the hill, \n"
            "and he massacred hundreds of towns people. \n"
            )

#Baker (town)

func = caller()

sequence = func[0]
max_length = func[1]




inputs = tokenizer.encode(sequence, return_tensors='pt')
outputs = model.generate(inputs, max_length, do_sample=True, temperature=0.3,top_p=0.9, top_k=50, no_repeat_ngram_size=2)
text = tokenizer.decode(outputs[0], skip_special_tokens=True,)
print(len(text))


points = ['!', '?', '.']
text_filter = text.replace("  ", " ")
textArray = text_filter.split('\n')
filtered = False

while(filtered == False):

    if(textArray[-1].rstrip()[-1] not in points):
        textArray = textArray[0:-1]
    else:
        filtered = True

for i in range(len(textArray)):
    print(textArray[i])

