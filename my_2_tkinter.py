import tkinter as tk

root = tk.Tk() # instantiating the tk window

root.geometry('500x300') # sets the size of the window
root.configure(bg='pink') # sets the colour of the window

root.title("Hello World")
my_frist_label = tk.Label(root, text = "Hello World!", font=('Arial', 20), bg='pink')

my_frist_label.pack() # attaches the label to the window
root.mainloop()