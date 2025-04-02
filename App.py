import tkinter as tk
import tkinter as ttk
from Chart import Chart
from Start_page import Start_page
from Search import Search
from Login import Login
from Signup import Signup


root = tk.Tk()
root.title("Feelings Logger")

start = Start_page(root)
chart = Chart(root)
search = Search(root)
login = Login(root)
signup = Signup(root)

def show_main_frame():
    chart.chart_frame.grid_remove()
    search.search_frame.grid_remove()
    start.main_frame.grid(row=0, column=0, sticky="nsew")

def show_chart_frame():
    start.main_frame.grid_remove()
    search.search_frame.grid_remove()
    chart.chart_frame.grid(row=2, column=2, sticky="nsew")
    chart.plot_chart(1) 

def show_search_frame():
    chart.chart_frame.grid_remove()
    start.main_frame.grid_remove()
    search.search_frame.grid(row=0, column=0, sticky="nsew")
def show_login_frame():
    signup.signup_frame.grid_remove()
    login.login_frame.grid(row=0, column=0, sticky="nsew")
def show_signup_frame():
    login.login_frame.grid_remove()
    signup.signup_frame.grid(row=0, column=0, sticky="nsew")

#analysis button for showing chart
analysis_btn = ttk.Button(start.main_frame, text='Analysis', command = show_chart_frame)
analysis_btn.grid(row=5, column=3, pady=3)

search_btn = ttk.Button(start.main_frame, text='Filter', command = show_search_frame)
search_btn.grid(row=5, column=4, pady=3)

#button for going back to main frame
back_btn = ttk.Button(chart.chart_frame, text="← Back", command=show_main_frame)
back_btn.grid(row=1, column=1, sticky="w", padx=10, pady=5)

back_btn2= ttk.Button(search.search_frame, text="← Back", command=show_main_frame)
back_btn2.grid(row=1, column=1, sticky="w", padx=10, pady=5)

show_signup_frame() 
root.mainloop()