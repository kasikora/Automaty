import pygame
import button
from GUILife import game_of_life_simulation
from GUISand import sand_simulation
from GUITraffic import traffic_simulation

pygame.init()

WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Automaty")

game_of_life_image = pygame.image.load('texturepack/game_of_life_button.png').convert_alpha()
sand_simulator_image = pygame.image.load('texturepack/sand_simulator_button.png').convert_alpha()
traffic_simulator_image = pygame.image.load('texturepack/traffic_simulator_button.png').convert_alpha()
exit_image = pygame.image.load('texturepack/exit_button.png').convert_alpha()

background_img = pygame.image.load('texturepack/bc6.jpg').convert_alpha()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Zmiana rozmiaru tła
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
width_half = WIDTH/2
height_part = HEIGHT*0.7/4
screen.blit(background_img, (0, 0))

game_of_life_button = button.Button(width_half - game_of_life_image.get_rect().centerx*0.5, height_part, game_of_life_image, 0.5)
sand_simulator_button = button.Button(width_half - sand_simulator_image.get_rect().centerx*0.4, height_part*2, sand_simulator_image, 0.4)
traffic_simulator_button = button.Button(width_half - traffic_simulator_image.get_rect().centerx*0.4, height_part*3, traffic_simulator_image, 0.4)
exit_button = button.Button(width_half - exit_image.get_rect().centerx*0.4, height_part*4, exit_image, 0.4)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif game_of_life_button.draw(screen):
            try:
                game_of_life_simulation(100, 10)
            except Exception as e:
                print(f"Błąd: {e}")
        elif sand_simulator_button.draw(screen):
            try:
                sand_simulation(100, 7,1,1)
            except Exception as e:
                print(f"Błąd: {e}")
        elif traffic_simulator_button.draw(screen):
            try:
                traffic_simulation(50, 20)
            except Exception as e:
                print(f"Błąd: {e}")
        elif exit_button.draw(screen):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Wciśnięcie klawisza "R" spowoduje zmianę rozdzielczości
                new_width = 1600
                new_height = 400
                traffic_simulator_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                game_of_life_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                sand_simulator_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                exit_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                WIDTH = new_width
                HEIGHT = new_height
                # Zakończ obecne okno
                pygame.display.quit()

                # Utwórz nowe okno z nowymi wymiarami
                screen = pygame.display.set_mode((new_width, new_height))
                background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Zmiana rozmiaru tła
                screen.blit(background_img, (0, 0))

    # Umieść tło na ekranie przed rysowaniem przycisków



    pygame.display.flip()

pygame.quit()
