import csv

class State:
    def __init__(self, no, content, wipe, story, next_state_no):
        self.story = story
        self.no = no #scene no
        self.content = list(content) #scene content names
        self.wipe = wipe #wipe the contents of the last scene
        self.next_state = list()
        for no in next_state_no: self.next_state.append(self.story.get_state(no)  ) #next state no

    def prep_state(self):
        #smth smth wipe screen
        return

class Prompt(State):
    def __init__(self):
        self.choices = self.content
        
    def prep_state(self):
        return

    def get_state_from_question(self):
        #smth smth get input
        input = ""
        match input:
            case self.content[0]: return self.next_state[0]
            case self.content[1]: return self.next_state[1]
            case self.content[2]: return self.next_state[2]
            case self.content[3]: return self.next_state[3]

class Image(State):
    def __init__(self):
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
    def __init__(self):
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
                    newState = CutScene(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"])])
                elif (scene["Type"]=="Image"):
                     newState = Image(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"])])
                elif (scene["Type"]=="Prompt"):
                    newState = Prompt(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"]),int(scene["NextState1"]),int(scene["NextState2"]),int(scene["NextState3"])])
                else:
                    newState = State(no = scene["SceneNo"],
                                    content = [scene["Content0"],scene["Content1"],scene["Content2"],scene["Content3"]],
                                    wipe = (scene["Wipe"]=="TRUE"),
                                    story = self,
                                    next_state_no=[int(scene["NextState0"])])
                newState.prepState()
                self.story.append(newState)

    def get_state(self, state_no):
        for state in self.states:
            if int(state["SceneNo"]) == state_no:
                return state
