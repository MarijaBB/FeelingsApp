import tkinter as tk
from Signup import Signup
#from Start_page import Start_page

root = tk.Tk()
root.title("Feelings Logger")

#start_page = Start_page(root,6)
signup = Signup(root)
root.mainloop()