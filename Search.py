import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from model.Search_methods import *
from model.Feelings_methods import getFeelings

class Search:
    def __init__(self, root, userId):
        self.search_frame = tk.Frame(root)
        self.userId = userId
        
        back_btn2 = ttk.Button(self.search_frame, text="← Back", command=lambda: self.go_back_to_main(root, userId))
        back_btn2.grid(row=6, column=3, sticky="w", padx=10, pady=5)
        self.search_frame.grid(row=0, column=0, sticky="nsew")
        self.make_search_page()
        
    def make_search_page(self):
        #filter for feeling
        ttk.Label(self.search_frame, text="Feelings:").grid(row=0, column=0, sticky="w")
        self.feeling_var = tk.StringVar()
        self.feeling_dropdown = ttk.Combobox(self.search_frame, textvariable=self.feeling_var, state="readonly")
        self.feeling_dropdown['values'] = getFeelings()
        
        self.feeling_dropdown.grid(row=0, column=1, padx=10)

        self.feeling_button = ttk.Button(self.search_frame, text="Filter by feeling", command=self.search_by_feeling)
        self.feeling_button.grid(row=0, column=2)

        #filter for period
        ttk.Label(self.search_frame, text="From Date:").grid(row=1, column=0, sticky="w", pady=10)
        self.from_date = DateEntry(self.search_frame, date_pattern='dd/mm/yyyy')
        self.from_date.grid(row=1, column=1, padx=10)

        ttk.Label(self.search_frame, text="To Date:").grid(row=2, column=0, sticky="w")
        self.to_date = DateEntry(self.search_frame, date_pattern='dd/mm/yyyy')
        self.to_date.grid(row=2, column=1, padx=10)

        self.date_button = ttk.Button(self.search_frame, text="Filter by period", command=self.search_by_date)
        self.date_button.grid(row=2, column=2,padx=10,pady=10)
        
        self.df_button = ttk.Button(self.search_frame, text="Filter by feeling\n for period", command=self.search_by_feeling_and_period)
        self.df_button.grid(row=3, column=2,padx=10)

        # result text box
        ttk.Label(self.search_frame, text="Results:").grid(row=4, column=0, sticky="w", pady=10)
        self.result_box = tk.Text(self.search_frame, height=10, width=50)
        self.result_box.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        self.result_box.config(state='disabled')

    def search_by_feeling(self):
        feeling = self.feeling_var.get()
        results = find_dates_for_feeling(self.userId,feeling)
        output = '\n'.join(map(str, results))
        
        self.result_box.config(state='normal')
        self.result_box.delete('1.0', tk.END)
        self.result_box.insert(tk.END, output)
        self.result_box.config(state='disabled')

    def search_by_date(self):
        from_date = self.from_date.get()
        to_date = self.to_date.get()
        results = find_feelings_for_dates(self.userId, from_date, to_date)
        output = '\n'.join(map(str, results))
        
        self.result_box.config(state='normal')
        self.result_box.delete('1.0', tk.END)
        self.result_box.insert(tk.END, output)
        self.result_box.config(state='disabled')
        
    def search_by_feeling_and_period(self):
        feeling = self.feeling_var.get()
        results = find_dates_for_feeling_in_period(self.userId, self.from_date.get(), self.to_date.get(), feeling)
        output = '\n'.join(map(str, results))
        
        self.result_box.config(state='normal')
        self.result_box.delete('1.0', tk.END)
        self.result_box.insert(tk.END,output)
        self.result_box.config(state='disabled')
    
    def go_back_to_main(self, root, userId):
        from view.show_main_frame import go_to_main_frame
        go_to_main_frame(root, userId, self.search_frame)


    
        
