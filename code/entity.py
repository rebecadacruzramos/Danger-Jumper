import pygame
import os

class Entity:
    def __init__(self, x, y, image_path):
        full_path = os.path.join(os.path.dirname(__file__), '..', image_path)
        self.image = pygame.image.load(full_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
