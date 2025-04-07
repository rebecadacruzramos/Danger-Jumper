import sys
import os
sys.path.append(os.path.dirname(__file__))


from game_menu import Menu
import pygame


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Meu Jogo")
    menu = Menu(window)
    menu.run()
    pygame.quit()

if __name__ == "__main__":
    main()