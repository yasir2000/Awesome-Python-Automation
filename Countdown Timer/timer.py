import os
import time
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

# Load duration from environment variable
DURATION = int(os.getenv('COUNTDOWN_DURATION', '60'))  # Default to 60 seconds if not set


class TimeFormatter:
    """Class responsible for formatting time."""
    
    def format_time(self, seconds):
        hrs, rem = divmod(seconds, 3600)
        mins, secs = divmod(rem, 60)
        return f"{hrs:02}:{mins:02}:{secs:02}"


class Timer:
    """Base timer class with a countdown method."""
    
    def __init__(self, duration):
        self.duration = duration
        self.time_formatter = TimeFormatter()

    def countdown(self):
        while self.duration:
            timer_display = self.time_formatter.format_time(self.duration)
            print(timer_display, end='\r')
            time.sleep(1)
            self.duration -= 1
        self.time_up()

    def time_up(self):
        print('Time Up!')


if __name__ == "__main__":
    countdown_timer = Timer(duration=DURATION)
    countdown_timer.countdown()
