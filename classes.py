
class State:
    def __init__(self, story, room):
        self.story = story
        self.room = room

        self.prompt = None
        self.image = None
        self.cutscene = None

    def set_prompt(self, prompt):
        self.prompt = prompt

    def set_cutscene(self, cutscene):
        self.cutscene = cutscene

    def set_image(self, image):
        self.image = image



    def do_state(self):
        print('\nDoing state...', end='')
        print('in room ',self.room.name)

        if not self.prompt is None:
            self.story.set_next_state(self.prompt.get_state_from_question())

        if not self.cutscene is None:
            self.story.set_next_state(self.cutscene.do_cutscene())

        if not self.image is None:
            self.story.set_next_state(self.image.do_image())

class Prompt:
    def __init__(self, question, choices, states):
        self.question = question
        self.choices = choices
        self.states = states

    def get_state_from_question(self):
        print('Q: '+self.question)
        print('A: '+', '.join([str(i)+') '+choice for i,choice in enumerate(self.choices)]))
        answer = int(input('Choose a number:'))
        return self.states[answer]

class Image:
    def __init__(self, image_prompt, next_state):
        self.image_prompt = image_prompt
        self.next_state = next_state

    def do_image(self):
        print('Fetching an image with the prompt',self.image_prompt)
        print('Displaying image')
        print('Moving to next state')
        return self.next_state

class CutScene:
    def __init__(self, textstory, next_state):
        self.textstory = textstory
        self.next_state = next_state

    def do_cutscene(self):
        print(self.textstory)
        return self.next_state

class Room:
    def __init__(self, name):
        self.name = name



class Story:
    def __init__(self):
        self.next_state = None

    def get_next_state(self):
        return self.next_state

    def set_next_state(self, state):
        self.next_state = state