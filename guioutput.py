from tkinter import messagebox
messagebox.showinfo("Hello", "This is GUI output")
import tkinter as tk
from tkinter import messagebox

# Create the main window (required)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show the GUI message box
messagebox.showinfo("Hello", "This is GUI output")
