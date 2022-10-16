import re

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from ConvStarters import *

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')




def produceDialog(content):

    print("this is zero : ", content[0])
    print("this is one : ", content[1])
    sequence = content[1]
    max_length = int(content[0])

    inputs = tokenizer.encode(sequence, return_tensors='pt')
    outputs = model.generate(inputs, max_length, do_sample=True, temperature=0.3,top_p=0.9, top_k=50, no_repeat_ngram_size=2)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True,)

    points = ['!', '?', '.', '"']
    text_filter = text.replace("  ", " ")
    text_split = text_filter.split('\n')


    finalText = []

    for i in range(len(text_split)):
        if len(text_split[i].rstrip()) > 1:
            finalText.append(text_split[i])

    filtered = False

    while (filtered == False):

        str = finalText[-1].rstrip()
        if len(str) <= 1:
            del finalText[-1]
            str = finalText[-1].rstrip()
       # print("Loop "+str + " " + str[-1])

        if (str[-1] not in points):
            str_sp = re.findall('.*?[.!\?]', str)
            finalText[-1] = "".join(str_sp)
        else:
            filtered = True

    returnText = "\n".join(finalText)
    return returnText

produceDialog(townMan())

