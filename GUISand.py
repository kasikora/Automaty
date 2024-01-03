import pygame
import sys
import numpy
from sand_test import *
from PIL import Image

# Initialize Pygame
pygame.init()

# Set up the window
cell_size = 10
N = 100
width, height = N * cell_size, N * cell_size
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sand Simulator")

# Set up colors
black = (0, 0, 0)
white = (200, 200, 200)
grey = (50, 50, 50)
yellow = (204, 204, 0)

# Initialize matrix and game of life parameters
matrix = numpy.empty((N, N), dtype=Grain)
for i in range(N):
    for j in range(N):
        matrix[i, j] = Grain()

for i in range(N - 1):
    for j in range(N - 2):
        matrix[i, j + 1].left = matrix[i + 1, j - 1 + 1]
        matrix[i, j + 1].center = matrix[i + 1, j + 1]
        matrix[i, j + 1].right = matrix[i + 1, j + 1 + 1]

print(matrix)
all_sand = []
for i in range(10):
    for j in range(10):
        matrix[i, j + 10].val = 1
        all_sand.append(matrix[i, j + 10])
print("\n", matrix)
# all_sand.reverse()
print(all_sand)

all_sand = new_alive_list(matrix, N)

processed_image_path = "1.jpg"
binary_image = Image.open(processed_image_path)

# Variable to track mouse state
drawing = False

continuos_sim = 0
tick = 40
press = 0

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handle mouse events for drawing live cells
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                x, y = event.pos
                col = x // cell_size % N
                row = y // cell_size % N
                matrix[row, col].val = - matrix[row, col].val + 1
                all_sand.append(matrix[row, col])
                print(matrix[row, col])
                all_sand = new_alive_list(matrix, N)#cos

        elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos
            col = x // cell_size % N
            row = y // cell_size % N
            matrix[row, col].val = - matrix[row, col].val + 1
            all_sand.append(matrix[row, col])
            all_sand = new_alive_list(matrix, N)#cos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        # Handle SPACE key to run the simulation

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            all_sand = let_them_fall2(all_sand)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            continuos_sim = - continuos_sim + 1

    if continuos_sim == 1:
        all_sand = let_them_fall2(all_sand)

    window.fill(black)


    for i in range(N):
        for j in range(N):
            if matrix[i, j].val == 1:
                rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                pygame.draw.rect(window, yellow, rect)

    for i in range(N + 1):
        pygame.draw.line(window, grey, (i * cell_size, 0), (i * cell_size, height), 1)
        pygame.draw.line(window, grey, (0, i * cell_size), (width, i * cell_size), 1)

    pygame.display.flip()
    pygame.time.Clock().tick(tick)
