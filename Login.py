import tkinter as tk
from tkinter import ttk

class Login:
    def __init__(self, root):
        self.login_frame = tk.Frame(root)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        #self.make_login_page()