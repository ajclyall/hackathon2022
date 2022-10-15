from classes import State, Room, Story, Prompt




if __name__=='__main__':

    main_story = Story()

    room1 = Room('Living Room')
    roomEnd = Room('The free world')

    state3 = State(main_story, room1)
    state2 = State(main_story, room1)
    state1 = State(main_story, room1)
    start_state = State(main_story, room1)

    prompt1 = Prompt('Yes?', ['Yes','No'], [state1,start_state])
    prompt2 = Prompt('Yes again?', ['Yes','No'], [state2,start_state])
    prompt3 = Prompt('Surely not yes again?', ['Yes','Maybe','No'], [state3,state1,start_state])


    start_state.set_prompt(prompt1)
    state1.set_prompt(prompt2)
    state2.set_prompt(prompt3)
    
    while True:

        cur_state = main_story.get_next_state()
        if cur_state == None:
            cur_state = start_state
        
        if cur_state == state3:
            print('Finished Game')
            break

        cur_state.do_state()
