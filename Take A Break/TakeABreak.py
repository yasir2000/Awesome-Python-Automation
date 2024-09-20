# .env
# This file would contain environment variables.
TOTAL_BREAKS=3
BREAK_INTERVAL_HOURS=2
BREAK_URL="http://www.youtube.com"

import os
import time
import webbrowser
from dotenv import load_dotenv

class BreakStrategy:
    """Interface for break strategies."""
    def take_break(self):
        raise NotImplementedError("Must implement take_break method")

class YouTubeBreak(BreakStrategy):
    """Concrete implementation of a break strategy that opens YouTube."""
    def take_break(self):
        webbrowser.open(os.getenv("BREAK_URL"))
        print("Opened YouTube for break.")

class BreakScheduler:
    """Class to manage break scheduling."""
    def __init__(self, strategy: BreakStrategy):
        self.strategy = strategy
        self.total_breaks = int(os.getenv("TOTAL_BREAKS", 3))
        self.break_interval = int(os.getenv("BREAK_INTERVAL_HOURS", 2)) * 60 * 60

    def start_breaks(self):
        print("This program started on " + time.ctime())
        for _ in range(self.total_breaks):
            time.sleep(self.break_interval)
            self.strategy.take_break()

if __name__ == "__main__":
    load_dotenv()  # Load environment variables
    youtube_break = YouTubeBreak()
    break_scheduler = BreakScheduler(youtube_break)
    break_scheduler.start_breaks()
