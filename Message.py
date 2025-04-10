import json
import tkinter as tk
from model import Message_methods
class Message:
    def __init__(self,root):
        self.message_text = tk.Text(root,height=6,width=50, font=("Helvetica", 12, "italic"))
        self.message_text.grid(row=4, column=2, columnspan=3,pady=5,padx=5)
        self.message_text.config(state="disabled")
        
    def write_message(self,feelingId):
        try:
             (message,color) = Message_methods.findMessageforFeeling(feelingId)
        except Exception as e:
            message = f"Error reading messages: {e}"
            return

        self.message_text.config(state="normal")  # Temporarily make it editable

        self.message_text.delete(1.0, tk.END) # 1 means line number, 0 means column
        self.message_text.insert(tk.END, message)

        self.message_text.tag_configure(color, foreground=color)
        self.message_text.tag_add(color, "1.0", tk.END)
        
        self.message_text.config(state="disabled") # Make it non-editable for user input
