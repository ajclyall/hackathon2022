import csv
from textGeneration import *
import ai


class State:
    def __init__(self, story, id, wipe, content, next_state_ids):
        self.story = story
        self.id = id
        self.wipe = wipe

        self.content = content
        self.next_state_ids = next_state_ids

        self.state_change_ready = False
    
    def prep_state(self):
        return


class Prompt(State):
    def __init__(self, story, id, wipe, content, next_state_ids):
        super().__init__(story, id, wipe, content, next_state_ids)
        self.question = content[0]
        self.choices = content[1:]

    def do_state(self, app):
        app.write_text('Q: '+self.question+'\n')
        app.write_text('A: '+', '.join([str(i)+') '+choice for i,choice in enumerate(self.choices)])+'\n')
        app.start_inputing()

    def is_state_done(self, app, keyevent):
        if app.is_capturing and keyevent.keycode == 13:
            return True
        else:
            return False

    def finish_state(self, app):
        app.is_capturing = False
        answer = int(app.get_finished_input())
        next_state = self.story.find_state(self.next_state_ids[answer])
        self.story.set_next_state(next_state)
        self.state_change_ready = True

    def from_csv(story, id, wipe, content, next_state_ids):
        new_state = Prompt(story, id, wipe, content, next_state_ids)
        return new_state

    def prep_state(self):
        pass

class Image(State):
    def __init__(self, story, id, wipe, content, next_state_ids):
        super().__init__(story, id, wipe, content, next_state_ids)

    def do_state(self, app):
        app.clear_canvas()
        app.draw_image(self)
        app.image_margin = 515
        
        app.write_text('Some text like')

    def is_state_done(self, app, keyevent):
        if keyevent.char != '':
            return True
        else:
            return False

    def finish_state(self, app):
        next_state = self.story.find_state(self.next_state_ids[0])
        self.story.set_next_state(next_state)
        self.state_change_ready = True

    def from_csv(story, id, wipe, content, next_state_ids):
        new_state = Image(story, id, wipe, content, next_state_ids)
        return new_state

    def prep_state(self):
        pass

class CutScene(State):
    def __init__(self, story, id, wipe, content, next_state_ids):
        super().__init__(story, id, wipe, content, next_state_ids)
        self.textstory = content[1]
        self.prep_state()

    def do_state(self, app):
        if self.wipe:
            app.clear_canvas()
        app.delay_write_text(self.textstory+'\n\n')

    def is_state_done(self, keyevent):
        if keyevent.char != '':
            return True
        else:
            return False

    def finish_state(self):
        next_state = self.story.find_state(self.next_state_ids[0])
        self.state_change_ready = True

    def from_csv(story, id, wipe, content, next_state_ids):
        new_state = CutScene(story, id, wipe, content, next_state_ids)
        return new_state

    def prep_state(self):
        self.textstory = produceDialog(content=self.content)
        return

class Story:
    def __init__(self):
        self.next_state = None
        self.cur_state = None
        self.states = []

    def set_next_state(self, next_state):
        self.next_state = next_state

    def get_cur_state(self):
        return self.cur_state

    def set_cur_state(self, state):
        self.cur_state = state

    def read_states(self):
        with open('states.csv') as states_file:
            states = csv.DictReader(states_file)
            for state in states:
                if (state["TYPE"]=="CUTSCENE"):
                    new_state = CutScene.from_csv(self, int(state['ID']), (state['WIPE']=='TRUE'), state['CONTENT'].split('+'), [int(i) for i in state['NEXTSTATES'].split('+')])
                elif (state["TYPE"]=="IMAGE"):
                    new_state = Image.from_csv(self, int(state['ID']), (state['WIPE']=='TRUE'), state['CONTENT'].split('+'), [int(i) for i in state['NEXTSTATES'].split('+')])
                    ai.generate_image(new_state)
                elif (state["TYPE"]=="PROMPT"):
                    new_state = Prompt.from_csv(self, int(state['ID']), (state['WIPE']=='TRUE'), state['CONTENT'].split('+'), [int(i) for i in state['NEXTSTATES'].split('+')])

                new_state.prep_state()
                self.states.append(new_state)
                new_state = None

    def find_state(self, id):
        for state in self.states:
            if state.id == id:
                return state


