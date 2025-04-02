import tkinter as tk
from tkinter import ttk
from controller.signup import signup

class Signup:
    def __init__(self, root):
        self.signup_frame = tk.Frame(root)
        self.signup_frame.grid(row=0, column=0, sticky="nsew")
        self.make_signup_page()

    def make_signup_page(self):
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
        done_btn = ttk.Button(self.signup_frame, text="Done", command=lambda: self.signup_command(self.username_entry.get(),self.email_entry.get(),self.password_entry.get()))
        done_btn.grid(row=4, column=1, pady=10)
        
    def signup_command(self,username,email,password):
        k = signup(username, email, password)
        if k == 1: # successful signup
            print('successfull signup ')
            pass
            #show_login_frame()
        if k == 0:
            self.add_label('That username already exists. Try again...')
            self.make_signup_page()
        if k == -1:
            self.add_label('Email already exists...')
            self.make_signup_page()
        
    
    def add_label(self,text):
        ttk.Label(self.signup_frame, text=text).grid(row=7, column=1, padx=10, pady=5, sticky="e")
        
    
