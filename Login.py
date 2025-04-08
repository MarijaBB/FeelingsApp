import tkinter as tk
from tkinter import ttk
from model.Login_methods import *
from view.show_main_frame import go_to_main_frame
from view.write_label import add_label
from view.bind_enter_key import bind_enter

class Login:
    def __init__(self, root):
        self.login_frame = tk.Frame(root)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.make_login_page(root)

    def make_login_page(self,root):
        ttk.Label(self.login_frame, text="Log in", font=("Arial", 16)).grid(row=0, column=1, pady=10)

        # Email
        ttk.Label(self.login_frame, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self.login_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Password
        ttk.Label(self.login_frame, text="Password:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.label = add_label('',self.login_frame)
        # Done Button
        done_btn = ttk.Button(self.login_frame, text="Log in",
                              command=lambda: self.login_command(
                                                                  self.email_entry.get(),
                                                                  self.password_entry.get(),
                                                                  root))
        done_btn.grid(row=4, column=1, pady=10)
        
        bind_enter(self.password_entry, self.login_command,
           self.email_entry, self.password_entry, root = root)
        bind_enter(self.email_entry, self.login_command,
           self.email_entry, self.password_entry, root = root)

    def login_command(self,email,password,root):
        if check_if_email_exists(email) is not None:
            userId = check_is_password_correct(email,password)
            if userId is None:
                self.label.config(text = 'Wrong email or password...')
            else:
                go_to_main_frame(root, userId, self.login_frame)
                return            
        else:
            self.label.config(text = 'Wrong email or password...')