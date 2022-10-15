import csv

class State:
    def __init__(self, state_no, content, wipe, story, next_state_no):
        self.story = story
        self.no = state_no #scene no
        self.content = list(content) #scene content names
        self.wipe = wipe #wipe the contents of the last scene
        self.next_state = list()
        for no in next_state_no: self.next_state.append(self.story.find_state(no)  ) #next state no

    def prep_state(self):
        #smth smth wipe screen
        return

    def state_data(self):
        print("Scene No: ", self.no, "\n Scene Content: ", self.content, "\n Wipe?: ", self.wipe, "\n Next Scene No: ", self.next_state, "\n")

class Prompt(State):
    def __init__(self, state_no, content, wipe, story, next_state_no):
        State.__init__(self, state_no, content, wipe, story, next_state_no)
        self.choices = self.content
        
    def prep_state(self):
        return

    def get_state_from_question(self):
        #smth smth get input
        input = ""
        if input == self.content[0]:
            return self.next_state[0]
        elif input == self.content[1]:
            return self.next_state[1]
        elif input == self.content[2]:
            return self.next_state[2]
        elif input == self.content[3]:
            return self.next_state[3]

class Image(State):
    def __init__(self, state_no, content, wipe, story, next_state_no):
        State.__init__(self, state_no, content, wipe, story, next_state_no)
        self.image_prompt = self.content[0]
        self.image_name = self.content[1]
        self.next_state = self.next_state[0]

    def do_image(self):
        print('Fetching an image with the prompt',self.image_prompt)
        return self.next_state

    def prep_state(self):
        #smth smth generate image
        return

class CutScene(State):
    def __init__(self, state_no, content, wipe, story, next_state_no):
        State.__init__(self, state_no, content, wipe, story, next_state_no)
        self.textstory = str(self.content)
        self.next_state = self.next_state[0]

    def do_state(self):
        print(self.textstory)
        return self.next_state

    def prep_state(self):
        return


class Story:
    def __init__(self):
        self.next_state = None
        self.story = []

    def get_states(self):
        with open('scenes.csv') as scenes_file:
            scenes = csv.DictReader(scenes_file)
            for scene in scenes:
                if (scene["Type"]=="CutScene"):
                    newState = CutScene(state_no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"])])
                elif (scene["Type"]=="Image"):
                     newState = Image(state_no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"])])
                elif (scene["Type"]=="Prompt"):
                    newState = Prompt(state_no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"]),int(scene["NextState1"]),int(scene["NextState2"]),int(scene["NextState3"])])
                else:
                    newState = State(state_no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"])])
                newState.prep_state()
                self.story.append(newState)

    def find_state(self, state_no):
        for state in self.story:
            if int(state.no) == state_no:
                return state


