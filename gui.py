from imp import acquire_lock
import tkinter as tk
from random import randint
from threading import Lock


# from PIL.ImageTk import PhotoImage

from ai import generate_image


class GUI(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
       
        # Canvas Variables
        self.canvaswidth = 1000
        self.canvasheight = 428

        self.canvas = tk.Canvas(master, width=self.canvaswidth, height=self.canvasheight, bg="black", relief=tk.FLAT, bd=0)
       
        # Text Mode Variables
        self.cursorpos = (0,0)
        self.screen_width = 80
        self.screen_height = 25
        self.margin = 8
        self.lineheight = self.canvasheight//self.screen_height
        self.characterwidth = (self.canvaswidth-self.margin)//self.screen_width
        self.font = ('Courier','15','bold')



        self.image_margin = 0


        # Inputing text stuff
        self.input_list = []
        self.is_capturing = False

        self.canvas.pack(pady=200)

    def get_cursor_canvaspos(self):
        return (self.cursorpos[0]*self.characterwidth+self.margin+self.image_margin,self.cursorpos[1]*self.lineheight)

    def draw_character(self, char):
        if char == '\n':
            self.cursorpos = (0, self.cursorpos[1]+1)
        else:
            self.canvas.create_text(*self.get_cursor_canvaspos(), text=char, fill='white', font=self.font, anchor=tk.NW)
            self.cursorpos = (self.cursorpos[0]+1, self.cursorpos[1])


    def write_text(self,text):
        for char in text:
            self.draw_character(char)

    def delay_write_text(self, text):
        self.delay_draw_chars(list(text))

    def delay_draw_chars(self, list_chars):
        if len(list_chars) != 0:
            self.draw_character(list_chars.pop(0))
            self.after(randint(5,30), self.delay_draw_chars, list_chars)

    def start_inputing(self):
        self.input_list = []
        self.is_capturing = True

    def get_finished_input(self):
        self.is_capturing = False ## WARNING
        return ''.join(self.input_list)

    def store_char(self, char):
        self.input_list.append(char)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.cursorpos = (0,0)

    def draw_image(self, image_state):

        prompt = image_state.content
        file_name = image_state.id
        img = tk.PhotoImage(file=f'images/{file_name}.png')
        self.img = img ## SHEAR WITCHCRAFT
        self.canvas.create_image(self.get_cursor_canvaspos(), image=img, anchor=tk.NW)


        # self.image = ImageTk.PhotoImage(file=f"{slugify(prompt)}.png")
        # self.label.configure(image=self.image)


