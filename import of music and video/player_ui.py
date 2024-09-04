# player_ui.py
import os
import tkinter as tk
from tkinter import filedialog, ttk
from music_player import MusicPlayer
from video_player import VideoPlayer

class PlayerUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("420x300")
        self.root.minsize(420, 300)
        self.root.maxsize(420, 300)
        self.root.title("Media Player")

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, padx=20, pady=10)

        self.play_button = ttk.Button(self.button_frame, text="Play", command=self.play_media)
        self.pause_button = ttk.Button(self.button_frame, text="Pause", command=self.pause_media)
        self.stop_button = ttk.Button(self.button_frame, text="Stop", command=self.stop_media)

        self.play_button.grid(row=0, column=0, padx=10)
        self.pause_button.grid(row=0, column=1, padx=10)
        self.stop_button.grid(row=0, column=2, padx=10)

        self.media_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50)
        self.media_listbox.pack()

        self.choose_button = ttk.Button(self.root, text="Choose Directory", command=self.choose_directory)
        self.choose_button.pack()

        self.media_player = None

    def choose_directory(self):
        directory = filedialog.askdirectory()
        media_type = 'music'  # Or 'video' based on user input; this is just an example
        if media_type == 'music':
            self.media_player = MusicPlayer(directory)
        else:
            self.media_player = VideoPlayer(directory, pygame.display.set_mode((640, 480)))
        self.list_media_files()

    def list_media_files(self):
        self.media_listbox.delete(0, tk.END)
        for file in self.media_player.media_files:
            self.media_listbox.insert(tk.END, os.path.basename(file))

    def play_media(self):
        selected_item = self.media_listbox.curselection()
        if selected_item:
            index = int(selected_item[0])
            self.media_player.play(index)

    def pause_media(self):
        self.media_player.pause()

    def stop_media(self):
        self.media_player.stop()

    def run(self):
        self.root.mainloop()
