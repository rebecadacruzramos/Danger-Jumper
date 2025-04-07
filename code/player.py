import pygame
import os

class Player:
    def __init__(self, x, y):
        image = pygame.image.load(os.path.join('..', 'assets', 'player.png')).convert_alpha()
        self.image = pygame.transform.scale(image, (64, 64))  # Redimensionar imagem do player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = 500  # Alinha o player com o "chão"

        # Física
        self.vel_y = 0
        self.jump_force = -20
        self.gravity = 1
        self.jump_count = 0
        self.max_jumps = 2

        # Movimento lateral
        self.move_speed = 14

    def update(self, keys):
        # Movimento lateral
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.move_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.move_speed

        # Pulo
        if keys[pygame.K_SPACE] and self.jump_count < self.max_jumps:
            self.vel_y = self.jump_force
            self.jump_count += 1

        # Gravidade
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Colisão com o chão
        ground_level = 500
        if self.rect.bottom >= ground_level:
            self.rect.bottom = ground_level
            self.vel_y = 0
            self.jump_count = 0

    def draw(self, window):
        window.blit(self.image, self.rect)