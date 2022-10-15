import csv

class State:
    def __init__(self, story, id, content, next_state_ids):
        self.story = story
        self.id = id

        self.content = content
        self.next_state_ids = next_state_ids

        self.state_change_ready = False


class Prompt(State):
    def __init__(self, story, id, content, next_state_ids):
        super().__init__(story, id, content, next_state_ids)
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
        self.state_change_ready = True

    def from_csv(story, id, content, next_state_ids):
        new_state = Prompt(story, id, content, next_state_ids)
        return new_state

class Image(State):
    def __init__(self, story, id, content, next_state_ids):
        super().__init__(story, id, content, next_state_ids)

    def do_state(self, app):
        pass

    def finish_state(self, app):
        pass

    def from_csv(story, id, content, next_state_ids):
        new_state = Image(story, id, content, next_state_ids)
        return new_state

class CutScene(State):
    def __init__(self, story, id, content, next_state_ids):
        super().__init__(story, id, content, next_state_ids)
        self.textstory = content[0]

    def do_state(self, app):
        app.delay_write_text(self.textstory)
        app.write_text('\nPress any key to continue...\n')

    def is_state_done(self, keyevent):
        if keyevent.char != '':
            return True
        else:
            return False

    def finish_state(self):
        next_state = self.story.find_state(self.next_state_ids[0])
        self.state_change_ready = True

    def from_csv(story, id, content, next_state_ids):
        new_state = CutScene(story, id, content, next_state_ids)
        return new_state

class Story:
    def __init__(self):
        self.next_state = None
        self.cur_state = None
        self.states = []

    def get_cur_state(self):
        return self.cur_state

    def set_cur_state(self, state):
        self.cur_state = state

    def read_states(self):
        with open('states.csv') as states_file:
            states = csv.DictReader(states_file)
            for state in states:
                if (state["TYPE"]=="CUTSCENE"):
                    new_state = CutScene.from_csv(self, int(state['ID']), state['CONTENT'].split('+'), [int(i) for i in state['NEXTSTATES'].split('+')])
                elif (state["TYPE"]=="IMAGE"):
                    new_state = Image.from_csv(self, int(state['ID']), state['CONTENT'].split('+'), [int(i) for i in state['NEXTSTATES'].split('+')])
                elif (state["TYPE"]=="PROMPT"):
                    new_state = Prompt.from_csv(self, int(state['ID']), state['CONTENT'].split('+'), [int(i) for i in state['NEXTSTATES'].split('+')])

                self.states.append(new_state)

    def find_state(self, id):
        for state in self.states:
            if state.id == id:
                return state