import pygame
import os

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('..', 'assets', 'enemy.png')), (64, 64)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y  # Alinhado com o chão (ex: 500)
        self.speed = 4

    def update(self):
        self.rect.x -= self.speed
        # Reinicia inimigo ao sair da tela
        if self.rect.right < 0:
            self.rect.left = 800

    def draw(self, window):
        window.blit(self.image, self.rect)
