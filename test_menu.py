
import pygame
import button

pygame.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu w Pygame")
start_img = pygame.image.load('start_btn.png').convert_alpha()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

game_of_life_button = button.Button(300, 100, start_img, 0.8)
sand_simulator_button = button.Button(300, 250, start_img, 0.8)
traffic_simulator_button = button.Button(300, 400, start_img, 0.8)
quit_button = button.Button(300, 550, start_img, 0.8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif game_of_life_button.draw(screen):
            try:
                #pygame.quit()
                exec(open("GUILife.py").read())
            except Exception as e:
                print(f"Błąd: {e}")
        elif sand_simulator_button.draw(screen):
            try:
                exec(open("GUISand.py").read())
            except Exception as e:
                print(f"Błąd: {e}")
        elif traffic_simulator_button.draw(screen):
            try:
                exec(open("trafic_alg.py").read())
            except Exception as e:
                print(f"Błąd: {e}")
        elif quit_button.draw(screen):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Wciśnięcie klawisza "R" spowoduje zmianę rozdzielczości
                new_width = 1600
                new_height = 400
                traffic_simulator_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                game_of_life_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                sand_simulator_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                quit_button.scaling(WIDTH, HEIGHT, new_width, new_height)
                WIDTH = new_width
                HEIGHT = new_height
                # Zakończ obecne okno
                pygame.display.quit()

                # Utwórz nowe okno z nowymi wymiarami
                screen = pygame.display.set_mode((new_width, new_height))
                current_width, current_height = new_width, new_height

    pygame.display.flip()

pygame.quit()

#def add_buttons(window_height, window_width, num_of_buttons):
#    center =