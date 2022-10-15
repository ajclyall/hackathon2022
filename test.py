import csv
states = []

with open('scenes.csv') as scenes_file:
    scenes = csv.DictReader(scenes_file)
    for scene in scenes:
        states.append(scene)

for state in states:
    print(state)