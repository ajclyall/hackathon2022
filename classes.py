
class State:
    def __init__(self, story, room):
        self.story = story
        self.room = room

        self.prompt = None
        self.image = None
        self.cutscene = None

        self.state_change_ready = False

    def set_prompt(self, prompt):
        self.prompt = prompt

    def set_cutscene(self, cutscene):
        self.cutscene = cutscene

    def set_image(self, image):
        self.image = image


    def do_state(self, app):
        print('\nDoing state...', end='')
        print('in room ',self.room.name)

        if not self.prompt is None:
            self.prompt.do_prompt(app)

        if not self.cutscene is None:
            self.story.set_next_state(self.cutscene.do_cutscene(app))

        if not self.image is None:
            self.story.set_next_state(self.image.do_image(app))

        if not app.is_capturing:
            self.state_change_ready = True

    def finish_state(self, app):
        if not self.prompt is None:
            next_state = self.prompt.finish_prompt(app)
            print(next_state)
            print('YOU DIDNT EVEN REACH THIS POINT')
            self.story.set_next_state(next_state)
            self.state_change_ready = True


class Prompt:
    def __init__(self, question, choices, states):
        self.question = question
        self.choices = choices
        self.states = states

    def do_prompt(self, app):
        app.write_text('Q: '+self.question+'\n')
        app.write_text('A: '+', '.join([str(i)+') '+choice for i,choice in enumerate(self.choices)])+'\n')
        app.start_inputing()
        #answer = int(app.input_text()) ## INPUT VALIDATION NEEDED
        #print('This state is ready to move on :(')
        #return self.states[answer]

    def finish_prompt(self, app):
        answer = int(app.get_finished_input())
        return self.states[answer]

class Image:
    def __init__(self, image_prompt, next_state):
        self.image_prompt = image_prompt
        self.next_state = next_state

    def do_image(self, app):
        print('Fetching an image with the prompt',self.image_prompt)
        print('Displaying image')
        print('Moving to next state')
        return self.next_state

class CutScene:
    def __init__(self, textstory, next_state):
        self.textstory = textstory
        self.next_state = next_state

    def do_cutscene(self, app):
        app.delay_write_text(self.textstory)
        return self.next_state

class Room:
    def __init__(self, name):
        self.name = name



class Story:
    def __init__(self):
        self.next_state = None
        self.cur_state = None

    def get_next_state(self):
        return self.next_state

    def set_next_state(self, state):
        self.next_state = state

    def get_cur_state(self):
        return self.cur_state

    def set_cur_state(self, state):
        self.cur_state = state