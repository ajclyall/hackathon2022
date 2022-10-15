import tkinter as tk
from PIL import ImageTk, Image
from random import randint
#from ai import generate_image
#from django.utils.text import slugify


class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()


        """
        self.prompt_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.prompt_var)
        self.submit_button = tk.Button(master, text="submit", command=self.set_image)
        self.image = tk.PhotoImage(file='test.png')
        self.label = tk.Label(image=self.image)
        """

        # Canvas Variables
        self.canvaswidth = 1000
        self.canvasheight = 428

        self.canvas = tk.Canvas(master, width=self.canvaswidth, height=self.canvasheight, bg="black", relief=tk.FLAT, bd=0)
       
        # Text Mode Variables
        self.cursorpos = (0,0)
        self.screen_width = 80
        self.screen_height = 25
        self.lineheight = self.canvasheight//self.screen_height
        self.characterwidth = self.canvaswidth//self.screen_width
        self.font = ('Courier','15','bold')

        # Inputing text stuff
        self.input_list = []
        self.is_capturing = False

        #self.entry.pack()
        #self.label.pack()
        self.canvas.pack(pady=100)
        #self.submit_button.pack()

        #self.write_text('Hello world!\nThe end is nigh.')

    def get_cursor_canvaspos(self):
        return (self.cursorpos[0]*self.characterwidth,self.cursorpos[1]*self.lineheight)

    def draw_character(self, char):
        if char == '\n':
            self.cursorpos = (0, self.cursorpos[1]+1)
        else:
            self.canvas.create_text(*self.get_cursor_canvaspos(), text=char, fill='white', font=self.font, anchor=tk.NW)
            self.cursorpos = (self.cursorpos[0]+1, self.cursorpos[1])
        #time.sleep(0.05)

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

    def set_image(self):
        prompt = self.prompt_var.get()
        #generate_image(prompt)
        #self.image = ImageTk.PhotoImage(file=f"{slugify(prompt)}.png")
        self.label.configure(image=self.image)


