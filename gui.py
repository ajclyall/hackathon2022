from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self, root=None):
        self.text_frame = Frame(root)
        self.image_frame = Frame(root)


# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
