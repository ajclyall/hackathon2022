from gui import GUI, tk
from classes import Story

def update_state():
    cur_state = main_story.get_cur_state()
    if cur_state.state_change_ready:
        print('Changing state whooo')
        cur_state.state_change_ready = False
        main_story.set_cur_state(main_story.next_state)
        
        cur_state = main_story.get_cur_state()
        cur_state.do_state(app)
    

def key_pressed(event):
    cur_state = main_story.get_cur_state()
    print('Checking state',cur_state.id)
    if cur_state.is_state_done(app, event):
        print('State',cur_state.id, 'is done?')
        cur_state.finish_state(app)

    if app.is_capturing:
        if event.keycode != 13:
            app.draw_character(event.char)
            app.store_char(event.char)
    
    update_state()


if __name__=='__main__':

    main_story = Story()
    main_story.read_states()

    root = tk.Tk()
    root.attributes("-fullscreen", True) 
    root.config(bg='black')
    app = GUI(master=root)
    root.bind('<KeyPress>',key_pressed)

    start_state = main_story.find_state(0)

    main_story.set_cur_state(start_state)
    start_state.do_state(app)
    app.mainloop()
