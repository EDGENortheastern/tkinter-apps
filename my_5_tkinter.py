import tkinter as tk
from tkinter import ttk
import csv

class DogWalks(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tree = ttk.Treeview(self,
                                 columns=('Time', 'Dog'),
                                 show='headings')
        self.tree.heading('Time', text='Time')
        self.tree.heading('Dog', text='Dog')
        self.tree.pack()

        self.load_csv_data('dog_timetable.csv')

    def load_csv_data(self, filename):
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.tree.insert("", "end", values=(row['Time'], row['Dog']))

if __name__ == "__main__":
    app = DogWalks()
    app.mainloop()