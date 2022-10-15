from story import main_story, start_state, end_state
from gui import GUI, tk

def mainloop():
    cur_state = main_story.get_next_state()
    if cur_state == None:
        cur_state = start_state
    
    if cur_state == end_state:
        print('Finished Game')
        return False

    cur_state.do_state()

    return True

def update_state():
    cur_state = main_story.get_cur_state()
    #print(cur_state.state_change_ready)
    #print(cur_state==start_state)
    if cur_state.state_change_ready:
        cur_state.state_change_ready = False
        main_story.set_cur_state(main_story.next_state)

        cur_state = main_story.get_cur_state()
        #cur_state.state_change_ready = False
        cur_state.do_state(app)
    

def key_pressed(event):
    if event.keycode == 13:
        app.draw_character('\n')
    else:
        app.draw_character(event.char)

    update_state()


if __name__=='__main__':

    root = tk.Tk()
    root.config(bg='black')
    app = GUI(master=root)
    root.bind('<KeyPress>',key_pressed)

    main_story.set_cur_state(start_state)
    start_state.do_state(app)

    app.mainloop()
