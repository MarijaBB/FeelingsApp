from tkinter import ttk
def add_label(text,frame):
    ttk.Label(frame, text=text).grid(row=7, column=1, padx=10, pady=5, sticky="e")