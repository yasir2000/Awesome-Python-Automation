# music_player.py
import os
import pygame
from base_player import BasePlayer

class MusicPlayer(BasePlayer):
    def __init__(self, directory):
        super().__init__(directory)
        pygame.mixer.init()

    def load_media(self):
        pygame.mixer.music.load(self.current_file)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
