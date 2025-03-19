import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter, OrderedDict
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

HISTORY_FILE = "history.txt"

def read_history():
    try:
        file = open(HISTORY_FILE,"r", encoding="utf-8")
        feelings_list = [line[35:-1].lower() for line in file.readlines()]
    except FileNotFoundError as e:
            tk.messagebox.showerror("History file does not exist:\n{e}")
            return
    return  feelings_list

def plot_chart(chart_frame):
    feelings_list = read_history()

    if not feelings_list:
        messagebox.showinfo("No Data", "No feelings found in the history file.")
        return

    feeling_counts = Counter(feelings_list)
    sorted_feeling_counts = OrderedDict(sorted(feeling_counts.items(), key=lambda x: x[1]))
    
    feelings = list(sorted_feeling_counts.keys())
    counts = list(sorted_feeling_counts.values())

    
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    # bar chart
    axes[0].barh(feelings, counts, color=plt.cm.Pastel1.colors)
    axes[0].set_xlabel("Count")
    axes[0].set_ylabel("Feelings")
    axes[0].set_title("Feelings Frequency in History")
    #pie chart
    axes[1].pie(counts, labels=feelings, autopct="%1.1f%%", startangle=120, colors=plt.cm.Pastel1.colors)
    axes[1].set_title("Feeling Distribution")
    plt.tight_layout()
    
    global canvas
    if "canvas" in globals():
        canvas.get_tk_widget().destroy()  
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0,column=0, pady=5, padx=5)

   # plt.show()
     