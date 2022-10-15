
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from ConvStarters import *

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')




def produceDialog(func):

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


    #Try to set up a function that gets rid of random charecters

    return

