import os
import random
import time
import win32api
import win32con
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class IClickStrategy(ABC):
    """Strategy interface for different clicking strategies."""
    
    @abstractmethod
    def click(self, x: int, y: int):
        pass

class DefaultClickStrategy(IClickStrategy):
    """Default strategy to perform mouse clicks."""
    
    def click(self, x: int, y: int):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

class Clicker:
    """Facade for mouse clicking operations."""
    
    def __init__(self, strategy: IClickStrategy):
        self.strategy = strategy

    def perform_click(self):
        x = random.randint(0, int(os.getenv('SCREEN_WIDTH', 100)))
        y = random.randint(0, int(os.getenv('SCREEN_HEIGHT', 100)))
        self.strategy.click(x, y)

def main():
    click_strategy = DefaultClickStrategy()
    clicker = Clicker(click_strategy)
    
    delay_time = int(os.getenv('CLICK_DELAY', 15))
    
    while True:
        clicker.perform_click()
        time.sleep(delay_time)

if __name__ == "__main__":
    main()
