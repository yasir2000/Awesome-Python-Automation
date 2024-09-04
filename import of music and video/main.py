# main.py
import os
from dotenv import load_dotenv
from player_ui import PlayerUI

load_dotenv()

if __name__ == "__main__":
    player_ui = PlayerUI()
    player_ui.run()
