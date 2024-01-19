import pygame
import sys
from trafic_alg import *

pygame.init()

cell_size = 20

N = 22

matrix = make_road_matrix(N)
spawners = SpawnersListObject()

for i in range(N - 1):
    matrix[i, 10].neighbours.append(matrix[i + 1, 10])
for i in range(N - 1):
    matrix[i + 1, 11].neighbours.append(matrix[i, 11])
spawners.add_spawner(Spawner(matrix[0, 10], frequency_spawn_percentage_chance=3))
spawners.add_spawner(Spawner(matrix[N - 1, 11], frequency_spawn_percentage_chance=3))

for i in range(N - 1):
    matrix[11, i].neighbours.append(matrix[11, i + 1])
for i in range(N - 1):
    matrix[10, i + 1].neighbours.append(matrix[10, i])
spawners.add_spawner(Spawner(matrix[11, 0],3))
spawners.add_spawner(Spawner(matrix[10, N - 1], 3))

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

width, height = N * cell_size, N * cell_size
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Road traffic simulator")

# initial_board = black_and_white("3.JPG", "11.jpg", N)

black = (0, 0, 0)
white = (200, 200, 200)
grey = (50, 50, 50)
yellow = (204, 204, 0)
green = (82, 192, 78)
blue = (0, 0, 255)


# Variable to track mouse state
drawing = False

continuos_sim = 0
tick = 10
press = 0

draw_road =[]

for i in range(N):
    for j in range(N):
        if matrix[i, j].neighbours:
            if matrix[i, j] not in draw_road:
                draw_road.append(matrix[i, j].coords)
            for neighbour in matrix[i, j].neighbours:
                if neighbour not in draw_road:
                    draw_road.append(neighbour.coords)

print(draw_road)
print (len(draw_road))

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spawners.spawn_all(cars)
            crossroad1.give_orders()
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
        cars = cars_go(cars)

    window.fill(green)

    for road_coords in draw_road:
        rect = pygame.Rect(road_coords[1] * cell_size, road_coords[0] * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, grey, rect)

    for i in range(N):
        for j in range(N):
            if matrix[i, j].has_car == 1:
                rect_outer = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                rect_inner = pygame.Rect(j * cell_size + 3, i * cell_size + 3, cell_size - 6, cell_size - 6)

                pygame.draw.rect(window, white, rect_outer)
                pygame.draw.rect(window, blue, rect_inner)

    pygame.display.flip()
    pygame.time.Clock().tick(tick)
