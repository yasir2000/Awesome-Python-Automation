# video_player.py
import os
import pygame
from base_player import BasePlayer

class VideoPlayer(BasePlayer):
    def __init__(self, directory, display):
        super().__init__(directory)
        pygame.init()
        self.display = display

    def load_media(self):
        video = pygame.movie.Movie(self.current_file)
        video.set_display(self.display)
        video.play()

    def pause(self):
        # Implement pause functionality
        pass

    def resume(self):
        # Implement resume functionality
        pass

    def stop(self):
        # Implement stop functionality
        pass
