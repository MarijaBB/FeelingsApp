import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk  
from History import History
from Message import Message
from Chart import plot_chart

# Feelings and image files
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

# Main window
root = tk.Tk()
root.title("Feelings Logger")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10, "bold"))

# Create frames for the layout
top_frame = tk.Frame(root)
left_frame = tk.Frame(root)
right_frame = tk.Frame(root)
center_frame = tk.Frame(root)

top_frame.grid(row=0, column=2, columnspan=3,pady=5,padx=5)
left_frame.grid(row=1, column=1, rowspan=4,pady=5,padx=5)
right_frame.grid(row=1, column=6, rowspan=3,pady=5,padx=5)
center_frame.grid(row=1, column=2, columnspan=3,pady=5,padx=5)

root.grid_rowconfigure(0, weight=1)  
root.grid_rowconfigure(1, weight=0)  
root.grid_rowconfigure(2, weight=1)  

root.grid_columnconfigure(0, weight=1)  
root.grid_columnconfigure(1, weight=0)  
root.grid_columnconfigure(2, weight=1)  

# Store image references
images = {}


top_buttons = ["happy", "sad", "angry"]
left_buttons = ["bored", "calm", "concerned","tired"]
right_buttons = ["determined", "funky", "overstimulated", "socially anxious",]

def create_button(parent, feeling, img_file, row, column):
    try:
        image = Image.open(img_file)
        image = image.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        images[feeling] = photo  # Keep reference
        btn = ttk.Button(parent, image=photo, text=feeling, compound="top",
                        command=lambda f=feeling: (history.add_entry(f), message.write_message(f)))
        btn.grid(row=row, column=column, pady=5)  # Position button in grid
    except Exception as e:
        print(f"Error loading image for {feeling}: {e}")

for i, feeling in enumerate(top_buttons):
    create_button(top_frame, feeling, feelings[feeling], 0, i)

# Create buttons for the left frame (1st column)
for i, feeling in enumerate(left_buttons):
    create_button(left_frame, feeling, feelings[feeling], i, 0)

# Create buttons for the right frame (3rd column)
for i, feeling in enumerate(right_buttons):
    create_button(right_frame, feeling, feelings[feeling], i, 0)

#Create button for chart
btn = ttk.Button(text='Analysis', command = plot_chart)
btn.grid(row=5, column=2, pady=5)

# history and message widgets in the center
history = History(center_frame)
history.show_history()

message = Message(center_frame)

root.mainloop()
history.file.close()
