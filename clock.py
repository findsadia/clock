import tkinter as tk
from tkinter import font
import time

class SimpleClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Clock Application")
        self.root.geometry("300x100")
        self.root.configure(bg="black")
        
        self.time_label = tk.Label(self.root, font=('Helvetica', 48), fg='white', bg='black')
        self.time_label.pack(anchor='center')
        
        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleClockApp(root)
    root.mainloop()
