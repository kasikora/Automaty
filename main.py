import pygame
from test_menu import menu
from GUITraffic import traffic_simulation
from GUILife import game_of_life_simulation
from GUISand import sand_simulation
def main():
    pygame.init()

    while True:
        choice = menu()

        if choice == "game_of_life":
            game_of_life_simulation(90, 10, 1, 1)
        elif choice == "sand_simulation":
            sand_simulation(100, 7, 1, 1)
        elif choice == "traffic_simulation":
            traffic_simulation(40, 20, 6)

        elif choice == "exit":
            break

    pygame.quit()

if __name__ == "__main__":
    main()
