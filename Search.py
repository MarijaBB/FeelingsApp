import tkinter as tk
from tkinter import ttk

# for better filtering history should be in table (sql) not in .txt
class Search:
    def __init__(self, root, userId):
        self.search_frame = tk.Frame(root)
        back_btn2 = ttk.Button(self.search_frame, text="← Back", command=lambda: self.go_back_to_main(root, userId))
        back_btn2.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        self.search_frame.grid(row=0, column=0, sticky="nsew")
    def go_back_to_main(self, root, userId):
        from view.show_main_frame import go_to_main_frame
        go_to_main_frame(root, userId, self.search_frame)


    
        
