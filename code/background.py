import pygame
import os

class Background:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'background.png')
        self.image = pygame.image.load(path).convert()

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
