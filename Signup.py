import tkinter as tk
from tkinter import ttk
from services.validation import *
from services.hash_password import hashing_password
from model.Login_methods import *
from view.show_login_frame import go_to_login_page
from view.write_label import add_label

class Signup:
    def __init__(self, root):
        self.signup_frame = tk.Frame(root)
        self.signup_frame.grid(row=0, column=0, sticky="nsew")
        self.make_signup_page(root)

    def make_signup_page(self,root):
        ttk.Label(self.signup_frame, text="Sign Up", font=("Arial", 16)).grid(row=0, column=1, pady=10)

        # Username
        ttk.Label(self.signup_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ttk.Entry(self.signup_frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Email
        ttk.Label(self.signup_frame, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self.signup_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Password
        ttk.Label(self.signup_frame, text="Password:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.signup_frame, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        
        # Done Button
        done_btn = ttk.Button(self.signup_frame, text="Done", 
                              command=lambda: self.signup_command(self.username_entry.get(),
                                                                  self.email_entry.get(),
                                                                  self.password_entry.get(),
                                                                  root))
        done_btn.grid(row=4, column=1, pady=10)
        # 
        self.label = add_label('',self.signup_frame)
        
        self.login_button = tk.Button(
            root,
            text="Already have an account?",
            fg="blue",
            bd=0,
            cursor="hand2",
            font=("Helvetica", 9, "underline"),
            activeforeground="blue",
            activebackground="white",
            command = lambda:(self.login_button.grid_remove(), go_to_login_page(root, self.signup_frame))
        )
        self.login_button.grid(row=5, column=2, pady=10)
       
        
    def signup_command(self, username, email, password, root): 
        password_hash = hashing_password(password)
        text = ''
        if not is_username_good_format(username):
           text = 'Bad format of username'
        elif check_if_username_exists(username) is not None:
           text = 'Username exists'
        elif not is_email_good_format(email):
           text = 'Bad format of email'
        elif check_if_email_exists(email) is not None:
           text = 'Email exists'
        elif not is_password_good_format(password):
           text = 'Bad format of password'
        else:
            new_user(username, email, password_hash)
            self.login_button.grid_remove()
            go_to_login_page(root, self.signup_frame)
            return
        self.label.config(text=text)
        
        return
        
        
    
