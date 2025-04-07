import pygame
from background import Background
from player import Player
from enemy import Enemy
import os


class Level:
    def __init__(self, window):
        import  time
        self.spawn_timer = 0
        self.spawn_delay = 2000
        self.last_spawn_time = pygame.time.get_ticks()
        self.window = window
        self.background = Background()
        self.player = Player(50, 500)

        # Inimigos reposicionados mais distantes para evitar colisão instantânea
        self.enemies = [Enemy(400,500), Enemy(600, 500)]

        # DEBUG: Exibir os retângulos para confirmar posições
        print("Player Rect:", self.player.rect)
        for i, enemy in enumerate(self.enemies):
            print(f"Enemy {i} Rect:", enemy.rect)

        self.entities = [self.background] + self.enemies
        self.font = pygame.font.Font(None, 60)
        self.game_over = False

        # Música de fundo
        music_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'music.wav')
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)  # Loop infinito

    def spawn_enemy(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.spawn_delay:
            new_enemy = Enemy(800, 500)  # Ajuste y conforme o chão
            self.enemies.append(new_enemy)
            self.last_spawn_time = current_time

    def check_collisions(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.game_over = True
                pygame.mixer.music.stop()

                # Som de game over (opcional)
                gameover_sound_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'gameover.wav')
                if os.path.exists(gameover_sound_path):
                    gameover_sound = pygame.mixer.Sound(gameover_sound_path)
                    gameover_sound.play()

    def show_game_over(self):
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        self.window.blit(text, (self.window.get_width() // 2 - text.get_width() // 2,
                                self.window.get_height() // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if self.game_over:
                self.show_game_over()
                return  # Volta ao menu

            self.player.update(keys)

            self.spawn_enemy()
            for enemy in self.enemies:
                enemy.update()  # Se seu Enemy não tiver isso, a gente já faz!

            self.check_collisions()

            # Desenha tudo
            self.background.draw(self.window)
            for enemy in self.enemies:
                enemy.draw(self.window)
            self.player.draw(self.window)

            pygame.display.update()
            clock.tick(60)

            # Debug: desenha os retângulos do player e inimigos
            pygame.draw.rect(self.window, (255, 0, 0), self.player.rect, 2)  # vermelho = player
            for enemy in self.enemies:
                pygame.draw.rect(self.window, (0, 255, 0), enemy.rect, 2)  # verde = inimigos

