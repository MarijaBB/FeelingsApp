import json
import tkinter as tk
import random

class Message:
    def __init__(self,root):
        try:
            file_json = open("messages.json","r", encoding = "utf-8")
            self.file = file_json
            self.messages = json.load(self.file)
           # self.content = json.load(self.file)
        except FileNotFoundError as e:
            tk.messagebox.showerror("File with messages does not exist:\n{e}")
            return
        self.message_text = tk.Text(root,height=10,width=50)
        self.message_text.pack(pady=10)
    def write_message(self,feeling):
        try:
            match feeling:
                case "Happy":
                    categoryf = "yay_messages"
                    color = "red_text"
                case "Angry":
                    categoryf = "calm_down_messages"
                    color = "blue_text"
                case "Sad":
                    categoryf = "cheer_up_messages"
                    color = "green_text"
            message = self.messages[categoryf][random.randint(0,len(self.messages[categoryf])-1)]
        except Exception as e:
            message = f"Error reading messages.json: {e}"

        self.message_text.delete(1.0, tk.END) # 1 means line number, 0 means column
        self.message_text.insert(tk.END, message)
        self.message_text.tag_configure(color, foreground=color.split("_")[0])
        self.message_text.tag_add(color, "1.0", tk.END)
