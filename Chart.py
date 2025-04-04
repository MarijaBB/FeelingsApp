import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter, OrderedDict
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model import History_methods

class Chart:
    def __init__(self, root, userId):
        self.chart_frame = tk.Frame(root)
        self.canvas = None
        self.userId = userId
        
        back_btn = ttk.Button(self.chart_frame, text="← Back", command=lambda: self.go_back_to_main(root, userId))
        back_btn.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        self.plot_chart()


    def plot_chart(self):
        list_feeling_time = History_methods.readHistory(self.userId)
        feelings_list = [i for (i,_) in list_feeling_time]

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
        axes[1].pie(counts, labels=feelings, autopct="%1.1f%%", startangle=110, colors=plt.cm.Pastel1.colors)
        axes[1].set_title("Feeling Distribution")
        plt.tight_layout()
        
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()  
        self.canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0,column=0, pady=5, padx=5)
        
    def go_back_to_main(self, root, userId):
        from view.show_main_frame import go_to_main_frame
        go_to_main_frame(root, userId, self.chart_frame)
