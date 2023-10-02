import tkinter as tk

class EmojiChooser(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")
        self.title("Moji Chooser")
        self.config(bg = "light green")

        self.emoji_dict = {"Happy": "😊",
                            "Sad": "😢",
                            "Angry": "😠",
                            "Surprised": "😮",
                            "Neutral": "😐",
                            "Winking": "😉",
                            "Crying": "😭",
                            "Laughing": "😂",
                            "Confused": "😕",
                            "Love": "😍"}
        
        # Create a list of emotions
        self.emotions_list = list(self.emoji_dict.keys())

        # Set the first emotion as the default value in the dropdown
        self.selected_emotion = tk.StringVar()
        self.selected_emotion.set(self.emotions_list[0])

        # Create and pack a label to instruct the user
        self.instructions_label = tk.Label(self,
                                           text = " Choose an emotion",
                                           font = ('Arial', 20),
                                           bg = "light green")
        self.instructions_label.pack(pady=10)

        # Create and pack a dropdown menu for emotion selection
        self.dropdown = tk.OptionMenu(self,
                                      self.selected_emotion,
                                      *self.emotions_list)
        self.dropdown.config(font=("Arial", 20), bg="light green")
        self.dropdown["menu"].config(font=("Arial", 20), bg="light green")
        self.dropdown.pack(padx=20, pady=20)

        # Create a button that will call the show_emoji method when clicked
        self.btn = tk.Button(self,
                             command=self.show_emoji,
                             text = "Get Emoji!",
                             font = ('Arial', 20),
                             bg = "light green")
        self.btn.pack(pady = 20)
    
        # Create and pack a label to display the selected emoji
        self.label_emoji = tk.Label(self,
                                    text = "",
                                    font = ('Arial', 100),
                                    bg = "light green")
        self.label_emoji.pack(pady = 10)

    def show_emoji(self):
        # Display the corresponding emoji in the label
        emotion = self.selected_emotion.get()
        emoji = self.emoji_dict.get(emotion, "")
        self.label_emoji.config(text=emoji)

app = EmojiChooser()
app.mainloop()