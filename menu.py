import sys
import random
import pygame
from GUILife import game_of_life_simulation

pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Automaty")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 36)


def draw_button(x, y, width, height, text, button_color, text_color):
    pygame.draw.rect(screen, button_color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)


def main_menu():
    # Przyciski w formie prostokątów
    game_of_life_button = pygame.Rect(200, 100, 400, 100)
    sand_simulator_button = pygame.Rect(200, 250, 400, 100)
    traffic_simulator_button = pygame.Rect(200, 400, 400, 100)
    quit_button = pygame.Rect(200, 550, 400, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if game_of_life_button.collidepoint(x, y):
                    try:
                        # exec(open("GUILife.py").read())
                        game_of_life_simulation(100, 10)
                    except Exception as e:
                        print(f"Błąd: {e}")
                elif sand_simulator_button.collidepoint(x, y):
                    try:
                        exec(open("GUISand.py").read())
                    except Exception as e:
                        print(f"Błąd: {e}")
                elif traffic_simulator_button.collidepoint(x, y):
                    try:
                        exec(open("trafic_alg.py").read())
                    except Exception as e:
                        print(f"Błąd: {e}")
                elif quit_button.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()


        screen.fill(BLACK)
        draw_button(200, 100, 400, 100, "Game of Life", (50, 205, 50), WHITE)
        draw_button(200, 250, 400, 100, "Sand simulator", (0, 0, 255), WHITE)
        draw_button(200, 400, 400, 100, "Traffic simulator", (255, 0, 0), WHITE)
        draw_button(200, 550, 400, 100, "Quit", (255, 255, 0), WHITE)

        pygame.display.flip()


main_menu()
