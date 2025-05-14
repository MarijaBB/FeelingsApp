import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
class WeatherIcon:
    def __init__(self, root):
        self.label_icon = tk.Label(root)
        self.label_icon.grid(row=0, column=6,pady=10)

    def display_icon(self,icon_url):
        if not icon_url:
            self.label_icon.config(text = " ")
            return
        try:
            icon_response = requests.get(icon_url)
            img_data = Image.open(BytesIO(icon_response.content)) # from bytes to Pil image object
            img_tk = ImageTk.PhotoImage(img_data)                 # from Pil image object to PhotoImage object of tkinter module
            self.label_icon.config(image=img_tk)
            self.label_icon.image = img_tk
        except Exception as e:
            print(f"Error fetching or displaying icon: {e}")
            self.label_icon.config(text=" ")



