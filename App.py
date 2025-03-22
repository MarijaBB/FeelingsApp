import tkinter as tk
import tkinter as ttk
from Chart import Chart
from Start_page import Start_page

root = tk.Tk()
root.title("Feelings Logger")

start = Start_page(root)
chart = Chart(root)

def show_main_frame():
    chart.chart_frame.grid_remove()
    start.main_frame.grid(row=0, column=0, sticky="nsew")

def show_chart_frame():
    start.main_frame.grid_remove()
    chart.chart_frame.grid(row=2, column=2, sticky="nsew")
    chart.plot_chart() 

#analysis button for showing chart
analysis_btn = ttk.Button(start.main_frame, text='Analysis', command = show_chart_frame)
analysis_btn.grid(row=5, column=3, pady=5)

#button for going back to main frame
back_btn = ttk.Button(chart.chart_frame, text="← Back", command=show_main_frame)
back_btn.grid(row=1, column=1, sticky="w", padx=10, pady=5)

show_main_frame() 
root.mainloop()
start.history.file.close()