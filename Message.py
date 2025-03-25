import json
import tkinter as tk
import random

class Message:
    def __init__(self,root):
        try:
            file_json = open("messages.json","r", encoding = "utf-8")
            self.file = file_json
            self.messages = json.load(self.file)
        except FileNotFoundError as e:
            tk.messagebox.showerror("File with messages does not exist:\n{e}")
            return
        self.message_text = tk.Text(root,height=6,width=50, font=("Helvetica", 12, "italic"))
        self.message_text.grid(row=4, column=2, columnspan=3,pady=5,padx=5)
        
    def write_message(self,feeling):
        try:
            categoryf = "messages_for_" + feeling
            color = self.color_of_message(feeling)
            message = self.messages[categoryf][random.randint(0,len(self.messages[categoryf])-1)]
        except Exception as e:
            message = f"Error reading messages.json: {e}"

        self.message_text.config(state="normal")  # Temporarily make it editable

        self.message_text.delete(1.0, tk.END) # 1 means line number, 0 means column
        self.message_text.insert(tk.END, message)

        self.message_text.tag_configure(color, foreground=color)
        self.message_text.tag_add(color, "1.0", tk.END)
        
        self.message_text.config(state="disabled") # Make it non-editable for user input

    def color_of_message(self, feeling):
        if feeling in ['happy','funky','calm','determined']:
            return 'orange'
        if feeling in ['bored','sad','socially anxious','concerned']:
            return 'green'
        return 'blue' ## ['angry','overstimulated','tired']
