import tkinter as tk

root = tk.Tk() # instantiating the tk window
root.title("Hello World")
my_frist_label = tk.Label(root, text = "Hello World!")

my_frist_label.pack()
root.mainloop()