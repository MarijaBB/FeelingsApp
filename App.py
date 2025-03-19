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

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# Create frames for the layout
top_frame = tk.Frame(main_frame)
left_frame = tk.Frame(main_frame)
right_frame = tk.Frame(main_frame)
center_frame = tk.Frame(main_frame)

top_frame.grid(row=0, column=2, columnspan=3,pady=5,padx=5)
left_frame.grid(row=1, column=1, rowspan=4,pady=5,padx=5)
right_frame.grid(row=1, column=6, rowspan=3,pady=5,padx=5)
center_frame.grid(row=1, column=2, columnspan=3,pady=5,padx=5)


chart_frame = tk.Frame(root)

# Store image references
images = {}

top_buttons = ["happy", "sad", "angry"]
left_buttons = ["bored", "calm", "concerned","tired"]
right_buttons = ["determined", "funky", "overstimulated", "socially anxious",]

def show_main_frame():
    chart_frame.grid_remove()
    main_frame.grid(row=0, column=0, sticky="nsew")

def show_chart_frame():
    main_frame.grid_remove()
    chart_frame.grid(row=2, column=2, sticky="nsew")
    plot_chart(chart_frame)  # Show chart inside chart_frame

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

#buttons for the left frame 
for i, feeling in enumerate(left_buttons):
    create_button(left_frame, feeling, feelings[feeling], i, 0)

#buttons for the right frame 
for i, feeling in enumerate(right_buttons):
    create_button(right_frame, feeling, feelings[feeling], i, 0)

#analysis button for showing chart
analysis_btn = ttk.Button(main_frame, text='Analysis', command = show_chart_frame)
analysis_btn.grid(row=5, column=3, pady=5)

#button for going back to main frame
back_btn = ttk.Button(chart_frame, text="← Back", command=show_main_frame)
back_btn.grid(row=1, column=1, sticky="w", padx=10, pady=5)

# history and message widgets in the center
history = History(center_frame)
history.show_history()

message = Message(center_frame)

show_main_frame() 
root.mainloop()
history.file.close()
