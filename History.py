import tkinter as tk
from datetime import datetime

HISTORY_FILE = "history.txt"

class History:
    def __init__(self,root):
        try:
            file = open(HISTORY_FILE,"r+", encoding="utf-8")
            self.file = file
        except FileNotFoundError as e:
            tk.messagebox.showerror("History file does not exist:\n{e}")
            return
        self.history_text = tk.Text(root, height=10, width=55, font=("Helvetica", 11))
        self.history_text.grid(row=2, column=2, columnspan=3,pady=5,padx=5)

    def add_entry(self,feeling):
        try:
            self.file.seek(0)
            history = self.file.read()
            new_entry = datetime.now().strftime("%d.%b %Y, %H:%M:%S")+" I am feeling "+feeling + "\n"
            updated_history = new_entry + history

            self.file.seek(0)
            self.file.write(updated_history)
            self.file.truncate()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not write to history.txt:\n{e}")
            return
        self.show_history()
    def show_history(self):
        try:
            self.file.seek(0)
            history = self.file.read()
        except Exception as e:
            history = f"Error reading history.txt: {e}"

        self.history_text.config(state="normal")

        self.history_text.delete(1.0, tk.END) #delete previous history
        self.history_text.insert(tk.END, history)

        last_entry_len = self.history_text.search("\n", "1.0", tk.END)

        self.history_text.tag_configure("highlighted_text", background = "pink", foreground="black")
        self.history_text.tag_configure("black_text", foreground="black")

        self.history_text.tag_add("highlighted_text", "1.0", last_entry_len)  # last_entry is highlighted
        self.history_text.tag_add("black_text", last_entry_len, tk.END)       # every other entry is just plain text

        self.history_text.config(state="disabled") #user input not allowed