import tkinter as tk
from PIL import ImageTk, Image
from ai import generate_image
from django.utils.text import slugify


class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.prompt_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.prompt_var)
        self.submit_button = tk.Button(root, text="submit", command=self.set_image)
        self.image = tk.PhotoImage(file='test.png')
        self.label = tk.Label(image=self.image)
        self.entry.pack()
        self.label.pack()
        self.submit_button.pack()

    def set_image(self):
        prompt = self.prompt_var.get()
        generate_image(prompt)
        self.image = ImageTk.PhotoImage(file=f"{slugify(prompt)}.png")
        self.label.configure(image=self.image)


root = tk.Tk()
app = GUI(master=root)
app.mainloop()
