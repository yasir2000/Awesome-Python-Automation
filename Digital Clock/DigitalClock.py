import tkinter as tk
from time import strftime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TimeProvider:
    """Provides the current time as a formatted string."""
    
    @staticmethod
    def get_current_time():
        return strftime('%H:%M:%S %p')

class ClockLabel:
    """Responsible for displaying the time on the GUI."""
    
    def __init__(self, parent):
        self.label = tk.Label(parent, font=('Courier New', 40), 
                               background=os.getenv("CLOCK_BACKGROUND", "red"),
                               foreground=os.getenv("CLOCK_FOREGROUND", "black"))
        self.label.pack(anchor='center')

    def update_time(self):
        current_time = TimeProvider.get_current_time()
        self.label.config(text=current_time)
        self.label.after(1000, self.update_time)

class DigitalClockApp:
    """The main application class which sets up the GUI."""
    
    def __init__(self):
        self.top = tk.Tk()
        self.top.title('Digital Clock')
        self.top.resizable(0, 0)
        self.clock_label = ClockLabel(self.top)

    def run(self):
        self.clock_label.update_time()
        self.top.mainloop()

if __name__ == "__main__":
    clock_app = DigitalClockApp()
    clock_app.run()
