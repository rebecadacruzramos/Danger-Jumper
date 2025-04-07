import pygame
from game import Game

class Menu:
    def __init__(self, window):
        self.window = window
        self.game = Game(window)
        self.running = True
        self.font = pygame.font.SysFont("Arial", 36)

    def run(self):
        while self.running:
            self.window.fill((0, 0, 0))
            text = self.font.render("Pressione ESPAÇO para jogar", True, (255, 255, 255))
            self.window.blit(text, (200, 250))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game.run()
                        self.running = False