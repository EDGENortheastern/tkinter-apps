import tkinter as tk
from tkinter import messagebox
import csv
import re
from datetime import datetime

class GuestRegister(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.geometry("600x500")
        self.title("Guest Register")
        self.config(bg="#ffb38a")

        # Define roles and lunch items
        self.roles = ["Guest", "Speaker", "Organizer"]
        self.lunch_items = {
            "Sandwich": "🥪",
            "Salad": "🥗",
            "Pizza": "🍕",
            "Pasta": "🍝"
        }

        # Initialize variables
        self.selected_role = tk.StringVar(value=self.roles[0])
        self.selected_lunch = tk.StringVar(value="Sandwich")
        self.guest_name = tk.StringVar()

        # Create and pack the widgets
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Name:", font=("Arial", 20), bg="#ffb38a").pack(pady=10)
        tk.Entry(self, textvariable=self.guest_name, font=("Arial", 20), bg="light yellow").pack(pady=10, padx=20, fill='x')
        tk.Label(self, text="Choose your Role:", font=("Arial", 20), bg="#ffb38a").pack(pady=10)
        
        optionmenu = tk.OptionMenu(self, self.selected_role, *self.roles)
        optionmenu.config(font=("Arial", 20), bg="#ffb38a")
        optionmenu["menu"].config(font=("Arial", 20), bg="#ffb38a")
        optionmenu.pack(pady=10, padx=20)
        
        frame = tk.Frame(self, bg="#e2e2e2")
        frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(frame, text="Choose your Lunch:", font=("Arial", 20), bg="#e2e2e2").grid(row=0, column=0, columnspan=2)
        for idx, (item, emoji) in enumerate(self.lunch_items.items(), start=1):
            tk.Radiobutton(frame, text=f"{emoji} {item}", value=item, variable=self.selected_lunch,
                           font=("Arial", 20), bg="#e2e2e2", anchor='w').grid(row=idx, column=0, sticky='w')
        
        tk.Button(self, text="Register", command=self.register_guest, font=("Arial", 20), bg="light green").pack(pady=20)

    def title_case(self, name: str) -> str:
        return name.title()

    def presence_check(self, name: str) -> bool:
        return bool(name)

    def name_length_check(self, name: str) -> bool:
        return 0 < len(name) <= 50

    def format_check(self, name: str) -> bool:
        pattern = re.compile(r"^[a-zA-Z-' ]+$")
        return bool(pattern.match(name))

    def construct_error_message(self, errors: list) -> str:
        return "\n".join(errors)

    def register_guest(self):
        name = self.guest_name.get().strip() 
        name = self.title_case(name)
        role = self.selected_role.get()
        lunch = self.selected_lunch.get()

        errors = []

        if not self.presence_check(name):
            errors.append("Name cannot be empty!")
        
        if not self.name_length_check(name):
            errors.append("Name should be between 1 and 50 characters long!")
        
        if not self.format_check(name):
            errors.append("Name should only contain letters, dashes, spaces, and apostrophes!")

        if errors:
            messagebox.showerror("Error", self.construct_error_message(errors))
            return
        
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open('guests.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, role, lunch, timestamp])

        messagebox.showinfo("Registration Successful", f"{name}, registered as {role}, has chosen {lunch} for lunch.")

app = GuestRegister()
app.mainloop()








