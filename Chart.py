import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter, OrderedDict

HISTORY_FILE = "history.txt"

def read_history():
    try:
        file = open(HISTORY_FILE,"r", encoding="utf-8")
        feelings_list = [line[35:-1].lower() for line in file.readlines()]
    except FileNotFoundError as e:
            tk.messagebox.showerror("History file does not exist:\n{e}")
            return
    return  feelings_list

def plot_chart():
    feelings_list = read_history()

    if not feelings_list:
        messagebox.showinfo("No Data", "No feelings found in the history file.")
        return

    feeling_counts = Counter(feelings_list)
    sorted_feeling_counts = OrderedDict(sorted(feeling_counts.items(), key=lambda x: x[1]))
    
    feelings = list(sorted_feeling_counts.keys())
    counts = list(sorted_feeling_counts.values())

    # bar chart
    plt.subplots(figsize=(10, 6)) 
    plt.barh(feelings, counts, color='#FFDAB9')
    plt.xticks(range(0, max(counts) + 1, 1))
    plt.xlabel("Count")
    plt.ylabel("Feelings")
    plt.title("Feelings Frequency in History")
    plt.show()
     