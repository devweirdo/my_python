import threading
import time
import tkinter as tk

class runtime:
    def __init__(self):
        self.label_time = tk.Label()
    
    def time(self):
        self.string = time.strftime('%H:%M:%S %p')
        self.label_time.config(text = self.string)
        self.label_time.after(1000,func=self.time)
  
    def run(self):
        self.label_time.pack()
        self.time()



    





