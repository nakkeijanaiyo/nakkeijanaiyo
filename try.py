import tkinter as tk
from tkinter import ttk

view = tk.Tk()

view.title('あいうえお')
view.geometry('500x500')

question = ttk.Label(view, width=30)
question.pack()

view.mainloop()