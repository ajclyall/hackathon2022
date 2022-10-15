
class State:
    def __init__(self, story, room):
        self.story = story
        self.room = room

        self.prompt = None

    def set_prompt(self, prompt):
        self.prompt = prompt


    def do_state(self):
        print('\nDoing state...', end='')
        print('in room ',self.room.name)

        self.story.set_next_state(self.prompt.get_state_from_question())
    
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