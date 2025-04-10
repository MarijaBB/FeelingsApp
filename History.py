import tkinter as tk
from model import History_methods

class History:
    def __init__(self,root):
        self.history_text = tk.Text(root, height=10, width=55, font=("Helvetica", 11))
        self.history_text.grid(row=2, column=2, columnspan=3,pady=5,padx=5)
        self.history_text.config(state="disabled")

    def add_entry(self,feelingId,userId):
        try:
            History_methods.insertIntoHistory(feelingId,userId)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not write to history:\n{e}")
            return
        self.show_history(userId)

    def show_history(self,userId):
        try:
            history = History_methods.readHistory(userId)
            history_formatted = History_methods.formatHistory(history) 
            last_entry = history_formatted[0]
            last_entry_len = len(last_entry)
            history_string = ''
            for line in history_formatted:
                history_string+=line
        except Exception as e:
            history = f"Error reading history: {e}"
            return

        self.history_text.config(state="normal")  # Temporarily enable it
        
        self.history_text.delete(1.0, tk.END) #delete previous history
        self.history_text.insert(tk.END, history_string)

        self.history_text.config(state="disabled")  # Temporarily enable it
        
        self.history_text.tag_configure("highlighted_text", background = "pink", foreground="black")
        self.history_text.tag_configure("black_text", foreground="black")

        self.history_text.tag_add("highlighted_text", "1.0", f"1.{last_entry_len}")  # last entry is highlighted
        self.history_text.tag_add("black_text", f"1.{last_entry_len}", tk.END)       # every other entry is just plain text
        
        
