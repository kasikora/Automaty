import pygame
import sys
import numpy
from trafic_alg import *
from PIL import Image
from photo_refactor import black_and_white

# Initialize Pygame
pygame.init()

# Set up the window
cell_size = 20

N = 22

matrix = make_road_matrix(N)
spawners = SpawnersListObject()

for i in range(N - 1):
    matrix[i, 10].neighbours.append(matrix[i + 1, 10])
for i in range(N - 1):
    matrix[i + 1, 11].neighbours.append(matrix[i, 11])
spawners.add_spawner(Spawner(matrix[0, 10], frequency_spawn_percentage_chance=20))
spawners.add_spawner(Spawner(matrix[N - 1, 11], frequency_spawn_percentage_chance=20))

for i in range(N - 1):
    matrix[11, i].neighbours.append(matrix[11, i + 1])
for i in range(N - 1):
    matrix[10, i + 1].neighbours.append(matrix[10, i])
#spawners.add_spawner(Spawner(matrix[11, 0], 20))
#spawners.add_spawner(Spawner(matrix[10, N - 1], 3))

cars = []
for i in spawners.list_of_spawners:
    print(i)

crossroad1 = OmniPresentCrossroad()

crossroad1.add_entrance(matrix[6, 10])
crossroad1.add_entrance(matrix[10, 15])
crossroad1.add_entrance(matrix[15, 11])
crossroad1.add_entrance(matrix[11, 6])

crossroad1.add_exit(matrix[6, 11])
crossroad1.add_exit(matrix[11, 15])
crossroad1.add_exit(matrix[15, 10])
crossroad1.add_exit(matrix[10, 6])

crossroad1.create_paths()

crossroad1.remove_path(matrix[6, 10], matrix[6, 11])
crossroad1.remove_path(matrix[10, 15], matrix[11, 15])
crossroad1.remove_path(matrix[15, 11], matrix[15, 10])
crossroad1.remove_path(matrix[11, 6], matrix[10, 6])

crossroad1.create_paths_and_vectors()
crossroad1.create_entrance_object_list()
crossroad1.create_my_roads()


width, height = N * cell_size, N * cell_size
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("AAAaaaAA_A_A_A_AAaaaaa__AAAA")

# initial_board = black_and_white("3.JPG", "11.jpg", N)

black = (0, 0, 0)
white = (200, 200, 200)
grey = (50, 50, 50)
yellow = (204, 204, 0)

# Variable to track mouse state
drawing = False

continuos_sim = 0
tick = 10
press = 0

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spawners.spawn_all(cars)
            crossroad1.give_orders()
            crossroad1.right_hand_rule()
            cars = cars_go(cars)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            continuos_sim = - continuos_sim + 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            for i in range(N):
                for j in range(N):
                    matrix[i, j].has_car = 0
            # cars = new_alive_list(matrix, N)  # cos

    if continuos_sim == 1:
        spawners.spawn_all(cars)
        crossroad1.give_orders()
        crossroad1.right_hand_rule()
        cars = cars_go(cars)

    window.fill(black)

    for i in range(N):
        for j in range(N):
            if matrix[i, j].has_car == 1:
                rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                pygame.draw.rect(window, yellow, rect)

    for i in range(N + 1):
        pygame.draw.line(window, grey, (i * cell_size, 0), (i * cell_size, height), 1)
        pygame.draw.line(window, grey, (0, i * cell_size), (width, i * cell_size), 1)

    pygame.display.flip()
    pygame.time.Clock().tick(tick)