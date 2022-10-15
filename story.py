from classes import State, Room, Story, Prompt, Image, CutScene

main_story = Story()




start_room = Room('This is the starting room.')
end_room = Room('This is the ending room.')


start_state = State(main_story, start_room)
start_spiel = State(main_story, start_room)
start_image = State(main_story, end_room)
end_state = State(main_story, end_room)


image1 = Image('A scary day job', end_state)

cutscene1 = CutScene("""
You live a very average life. Everyday is the same old shit.
You work in a very boring bank job as a useless intern, they
say one day you will make it in the business. Obviously they
lie.
""", start_image)

prompt1 = Prompt('Begin Game?',
                ['Yes','No'],
                [start_spiel, end_state])



start_image.set_image(image1)
start_state.set_prompt(prompt1)
start_spiel.set_cutscene(cutscene1)