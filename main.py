from story import main_story, start_state, end_state


def mainloop():
    cur_state = main_story.get_next_state()
    if cur_state == None:
        cur_state = start_state
    
    if cur_state == end_state:
        print('Finished Game')
        return False

    cur_state.do_state()

    return True



if __name__=='__main__':

    keep_running = True
    while keep_running:
        keep_running = mainloop()