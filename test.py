import csv, classes

story = classes.Story()
story.get_states()

for scene in story.story:
    scene.state_data()