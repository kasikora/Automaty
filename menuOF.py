import pygame
import sys
import numpy
from game_of_life_alg import omnipresent_perception, next_matrix, ar_insert

# Initialize Pygame
pygame.init()

# Set up the window
cell_size = 30
N = 30
width, height = N * cell_size, N * cell_size
window = pygame.display.set_mode((width, height + 40))
pygame.display.set_caption("Automaty")

# Set up colors
black = (0, 0, 0)
white = (200, 200, 200)
grey = (169, 169, 169)
yellow = (204, 204, 0)

# Initialize matrix and game of life parameters
matrix = numpy.zeros((N, N)).astype(numpy.int16)
testarr = numpy.array([[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
ar_insert(matrix, testarr, 10, 10)
data = omnipresent_perception()
dead_or_alive = data[0]
arr = data[1]

# Variable to track mouse state
drawing = False

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
        elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos
            col = x // cell_size
            row = y // cell_size
            matrix[row, col] = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        # Handle SPACE key to run the simulation
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            matrix = next_matrix(matrix, N, dead_or_alive, arr)


    window.fill(grey)

    # Draw background grid with slightly thinner grey borders
    for i in range(N):
        for j in range(N):
            rect_outer = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            pygame.draw.rect(window, grey, rect_outer, 1)  # Draw slightly thinner grey border

            rect_inner = pygame.Rect(j * cell_size + 1, i * cell_size + 1, cell_size - 2, cell_size - 2)
            pygame.draw.rect(window, white, rect_inner)  # Draw white rectangle

    # Draw live cells with slightly thinner white borders
    for i in range(N):
        for j in range(N):
            if matrix[i, j] == 1:
                rect_outer = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                pygame.draw.rect(window, grey, rect_outer, 1)  # Draw slightly thinner grey border

                rect_inner = pygame.Rect(j * cell_size + 2, i * cell_size + 2, cell_size - 4, cell_size - 4)
                pygame.draw.rect(window, black, rect_inner)  # Draw black rectangle

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(5)  # Adjust the speed as needed