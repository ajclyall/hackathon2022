import csv

class State:
    def __init__(self, no, content, wipe, story, room, next_state_no):
        self.story = story
        self.no = no #scene no
        self.content = content #scene content name
        self.wipe = wipe #wipe the contents of the last scene
        self.next_state = self.story.get_state(next_state_no)   #next state no
        self.room = room

        self.prompt = None
        self.image = None
        self.cutscene = None

    def set_prompt(self, content):
        self.prompt = content

    def set_cutscene(self, content):
        self.cutscene = content

    def set_image(self, content):
        self.image = content

    def do_state(self):
        print('\nDoing state...', end='')
        print('in room ',self.room.name)

        if not self.prompt is None:
            self.story.set_next_state(self.prompt.get_state_from_question())

        if not self.cutscene is None:
            self.story.set_next_state(self.cutscene.do_cutscene())

        if not self.image is None:
            self.story.set_next_state(self.image.do_image())

class Prompt(State):
    def __init__(self, states):
        self.choices = self.content
        self.states = states

    def get_state_from_question(self):
        print('A: '+', '.join([str(i)+') '+choice for i,choice in enumerate(self.choices)]))
        answer = int(input('Choose a number:'))
        return self.states[answer]

class Image(State):
    def __init__(self):
        self.image_prompt = self.content

    def do_image(self):
        print('Fetching an image with the prompt',self.image_prompt)
        print('Displaying image')
        print('Moving to next state')
        return self.next_state

class CutScene(State):
    def __init__(self):
        self.textstory = str(self.content)


    def do_cutscene(self):
        print(self.textstory)
        return self.next_state

class Room:
    def __init__(self, name):
        self.name = name



class Story:
    def __init__(self):
        self.next_state = None
        self.states = []

    def get_states(self):
        with open('scenes.csv') as scenes_file:
            scenes = csv.DictReader(scenes_file)
            for scene in scenes:
                if (scene["Type"]=="CutScene"):
                    newState = CutScene(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self)
                elif (scene["Type"]=="Image"):
                     newState = Image(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self)
                elif (scene["Type"]=="Prompt"):
                    newState = Prompt(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self)
                else:
                    newState = State(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self)
                
                self.states.append(newState)

    def get_state(self, state_no):
        for state in self.states:
            if int(state["SceneNo"]) == state_no:
                return state

    def get_next_state(self):
        return self.next_state

    def set_next_state(self, state):
        self.next_state = state