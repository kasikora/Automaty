import pygame
import sys
import numpy
from game_of_life_alg import omnipresent_perception, next_matrix, ar_insert
from photo_refactor import black_and_white
def game_of_life_simulation(N, cell_size):

    pygame.init()

    width, height = N * cell_size, N * cell_size
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Of Life")

    black = (0, 0, 0)
    white = (200, 200, 200)
    grey = (169, 169, 169)
    red = (255, 0, 0)

    initial_board = black_and_white("3.jpg", "11.jpg", N)
    matrix = initial_board
    data = omnipresent_perception()
    dead_or_alive = data[0]
    arr = data[1]

    drawing = False

    continuos_sim = 0
    tick = 40

    live_cells_count = numpy.sum(matrix)

    generation_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    x, y = event.pos
                    col = x // cell_size % N
                    row = y // cell_size % N
                    matrix[row, col] = 1

            elif event.type == pygame.MOUSEMOTION and drawing:
                x, y = event.pos
                col = x // cell_size % N
                row = y // cell_size % N
                matrix[row, col] = 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                matrix = next_matrix(matrix, N, dead_or_alive, arr)
                generation_count += 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                matrix[:,:] = 0
                generation_count = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS:
                if tick > 6:
                    tick = tick - 5
                print(tick)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS:
                if tick < 55:
                    tick = tick + 5
                print(tick)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
                continuos_sim = -continuos_sim + 1

        if continuos_sim == 1:
            matrix = next_matrix(matrix, N, dead_or_alive, arr)
            generation_count += 1

        window.fill(white)

        live_cells_count = 0

        for i in range(N):
            for j in range(N):
                if matrix[i, j] == 1:
                    rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                    pygame.draw.rect(window, black, rect)
                    live_cells_count = live_cells_count + 1

        for i in range(N + 1):
            pygame.draw.line(window, grey, (i * cell_size, 0), (i * cell_size, height), 1)
            pygame.draw.line(window, grey, (0, i * cell_size), (width, i * cell_size), 1)

        font = pygame.font.Font(None, 25)
        text_cells = font.render(f'Live cells: {live_cells_count}', True, red)
        text_generation = font.render(f'Generation: {generation_count}', True, red)
        window.blit(text_cells, (5, 5))
        window.blit(text_generation, (5, 50))

        pygame.display.flip()

        pygame.time.Clock().tick(tick)
