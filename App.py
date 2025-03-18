import tkinter as tk
from PIL import Image, ImageTk  # You'll need pillow installed
from History import History
from Message import Message
# Feelings and image files

feelings = {
    "Happy": "./images/happy.jpg",
    "Sad": "./images/sad.jpg",
    "Angry": "./images/angry.jpg"
}

#Main window
root = tk.Tk()
root.title("Feelings Logger")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

images = {} # references to images

for feeling, img_file in feelings.items():
    try:
        image = Image.open(img_file)
        image = image.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        images[feeling] = photo
        btn = tk.Button(button_frame,
                        image=photo,
                        text=feeling,
                        compound="top",
                        command=lambda f=feeling: (history.add_entry(f),
                                                   message.write_message(f)))

        btn.pack(side="left", padx=10)
    except Exception as e:
        print(f"Error loading image for {feeling}: {e}")


history = History(root)
history.show_history()

message = Message(root)

root.mainloop()
history.file.close()
