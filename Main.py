import tkinter as tk
from tkinter import ttk
from gui import PumpFunApiGUI

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Red.TButton", background="red", foreground="white")
    style.configure("Green.TButton", background="green", foreground="white")
    style.configure("Orange.TButton", background="orange", foreground="black")
    app = PumpFunApiGUI(root)
    root.mainloop()