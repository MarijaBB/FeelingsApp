import tkinter as tk
from PIL import Image, ImageTk  
from tkinter import ttk
from History import History
from Message import Message

class Start_page:
    def __init__(self, root):
        self.main_frame = tk.Frame(root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.make_buttons()

    def make_buttons(self):
        feelings = {
            "happy": "./images/happy.jpg",
            "sad": "./images/sad.jpg",
            "angry": "./images/angry.jpg",
            "bored": "./images/bored.jpg",
            "calm": "./images/calm.jpg",
            "concerned": "./images/concerned.jpg",
            "determined": "./images/determined.jpg",
            "funky": "./images/funky.jpg",
            "overstimulated": "./images/overstimulated.png",
            "socially anxious": "./images/socially anxious.jpg",
            "tired": "./images/tired.png"
        }
        self.images = {}

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10, "bold"))

        top_buttons = ["happy", "sad", "angry"]
        left_buttons = ["bored", "calm", "concerned","tired"]
        right_buttons = ["determined", "funky", "overstimulated", "socially anxious"]
        
        top_frame = tk.Frame(self.main_frame)
        left_frame = tk.Frame(self.main_frame)
        right_frame = tk.Frame(self.main_frame)
        center_frame = tk.Frame(self.main_frame)

        top_frame.grid(row=0, column=2, columnspan=3,pady=5,padx=5)
        left_frame.grid(row=1, column=1, rowspan=4,pady=5,padx=5)
        right_frame.grid(row=1, column=6, rowspan=3,pady=5,padx=5)
        center_frame.grid(row=1, column=2, columnspan=3,pady=5,padx=5)

        self.history = History(center_frame)
        self.history.show_history()

        self.message = Message(center_frame)

        for i, feeling in enumerate(top_buttons):
            self.create_button(top_frame, feeling, feelings[feeling], 0, i)

        #buttons for the left frame 
        for i, feeling in enumerate(left_buttons):
            self.create_button(left_frame, feeling, feelings[feeling], i, 0)

        #buttons for the right frame 
        for i, feeling in enumerate(right_buttons):
            self.create_button(right_frame, feeling, feelings[feeling], i, 0)

    def create_button(self, parent, feeling, img_file, row, column):
        try:
            image = Image.open(img_file)
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.images[feeling] = photo  # Keep reference
            btn = ttk.Button(parent, image=photo, text=feeling, compound="top",
                            command=lambda f=feeling: (self.history.add_entry(f), self.message.write_message(f)))
            btn.grid(row=row, column=column, pady=5)  # Position button in grid
        except Exception as e:
            print(f"Error loading image for {feeling}: {e}")

            