import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Window App")
    window.geometry("300x200")
    label = tk.Label(window, text="Hello! This is a simple window.")
    label.pack(pady=50)
    window.mainloop()

create_window()import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Window App")
    window.geometry("300x200")
    label = tk.Label(window, text="Hello! This is a simple window.")
    label.pack(pady=50)
    window.mainloop()

create_window()