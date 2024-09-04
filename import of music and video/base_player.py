# base_player.py
import os
import pygame

class BasePlayer:
    def __init__(self, directory):
        self.directory = directory
        self.media_files = []
        self.current_file = None
        self.load_files()

    def load_files(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                self.media_files.append(os.path.join(root, file))

    def play(self, index):
        self.current_file = self.media_files[index]
        self.load_media()

    def load_media(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def pause(self):
        raise NotImplementedError()

    def resume(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()
