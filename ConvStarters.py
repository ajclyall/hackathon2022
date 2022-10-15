#THINGS THAT WILL CHANGE IN EACH CASE

#input text
#length of answer
max_length = 0
name = "emma" #user input

#town
def townMan():
    max_length = 150
    sequence = ("Hi my name is James \n"
                "I know you inherited the castle \n"
                "Have you heard the infinite horror stories about the bloody viscount \n"
                "He used to live in the castle on the hill, \n"
                "and he massacred hundreds of towns people. \n"
                )
    return sequence, max_length

#Baker (town)
def backer():
    max_length = 50
    sequence = (
                )
    return sequence, max_length

#big city
def caller():
    max_length = 100
    sequence = ("Hello "+ name + ", I am Georege \n"
                "I am calling you to let you know you have an inheritance waiting for you in the south of France. \n"
                "If you have any questions"
                )
    return sequence, max_length