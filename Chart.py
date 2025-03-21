import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter, OrderedDict
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

HISTORY_FILE = "history.txt"

class Chart:
    def __init__(self, root):
        self.chart_frame = tk.Frame(root)
        self.canvas = None

    def read_history(self):
        try:
            file = open(HISTORY_FILE,"r", encoding="utf-8")
            feelings_list = [line[35:-1].lower() for line in file.readlines()]
        except FileNotFoundError as e:
                tk.messagebox.showerror("History file does not exist:\n{e}")
                return
        return  feelings_list

    def plot_chart(self):
        feelings_list = self.read_history()

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
        
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()  
        self.canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0,column=0, pady=5, padx=5)

        