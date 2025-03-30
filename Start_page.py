import tkinter as tk
from PIL import Image, ImageTk  
from tkinter import ttk
from History import History
from Message import Message
from model import Feelings_methods
# login logic required, for now I use UserId = 1
class Start_page:
    def __init__(self, root):
        self.main_frame = tk.Frame(root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.userId = 1
        self.make_buttons()

    def make_buttons(self):   
        self.images = {}

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10, "bold"))

        top_buttons = [1,2,3]
        left_buttons = [4,5,6,11]
        right_buttons = [7,8,9,10]
        
        top_frame = tk.Frame(self.main_frame)
        left_frame = tk.Frame(self.main_frame)
        right_frame = tk.Frame(self.main_frame)
        center_frame = tk.Frame(self.main_frame)

        top_frame.grid(row=0, column=2, columnspan=3,pady=5,padx=5)
        left_frame.grid(row=1, column=1, rowspan=4,pady=5,padx=5)
        right_frame.grid(row=1, column=6, rowspan=3,pady=5,padx=5)
        center_frame.grid(row=1, column=2, columnspan=3,pady=5,padx=5)

        self.history = History(center_frame)
        self.history.show_history(self.userId)

        self.message = Message(center_frame)

        for i, feelingId in enumerate(top_buttons):
            self.create_button(top_frame, feelingId, Feelings_methods.getImage(feelingId), 0, i)

        #buttons for the left frame 
        for i, feelingId in enumerate(left_buttons):
            self.create_button(left_frame, feelingId, Feelings_methods.getImage(feelingId), i, 0)

        #buttons for the right frame 
        for i, feelingId in enumerate(right_buttons):
            self.create_button(right_frame, feelingId, Feelings_methods.getImage(feelingId), i, 0)

    def create_button(self, parent, feelingId, img_file, row, column):
        try:
            image = Image.open(img_file)
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.images[feelingId] = photo  # Keep reference
            btn = ttk.Button(parent, image=photo, text=Feelings_methods.getFeelingName(feelingId), compound="top",
                            command=lambda f=feelingId: (self.history.add_entry(f, self.userId), self.message.write_message(f)))
            btn.grid(row=row, column=column, pady=5)  # Position button in grid
        except Exception as e:
            print(f"Error loading image for {Feelings_methods.getFeelingName()}: {e}")

            