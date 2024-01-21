from tkinter.simpledialog import askinteger

import pygame
import sys
import numpy
from sand_test import *
from PIL import Image
from photo_refactor import black_and_white
import button

import tkinter as tk
from tkinter import filedialog


def sand_simulation(N, cell_size, scale_width, scale_height):

    pygame.init()

    width, height = N * cell_size, N * cell_size
    button_window_width = width * 0.4
    window = pygame.display.set_mode((width + button_window_width, height))
    pygame.display.set_caption("Sand Simulator")

    game_area = window.subsurface(pygame.Rect((0, 0, width, height)))

    initial_board = black_and_white("3.JPG", N)

    simtype_img = pygame.image.load('texturepack/simtype_sand.jpg').convert_alpha()
    resize_img = pygame.image.load('texturepack/resize_sand.jpg').convert_alpha()
    picture_img = pygame.image.load('texturepack/picture_sand.jpg').convert_alpha()
    clear_img = pygame.image.load('texturepack/clear_sand.jpg').convert_alpha()
    menu_img = pygame.image.load('texturepack/menu.jpg').convert_alpha()

    button_width = 100 * scale_width
    button_height = 50 * scale_height
    button_margin = 20 * scale_height

    total_button_height = 6 * (button_height + button_margin)
    button_scale = 0.6 * (scale_height + scale_width)/2
    simulation_button = button.Button(width + button_margin, (height - total_button_height) // 2, simtype_img, button_scale)
    reset_button = button.Button(width + button_margin,
                                 (height - total_button_height) // 2 + (button_height + button_margin), clear_img, button_scale)
    resize_button = button.Button(width + button_margin,
                                  (height - total_button_height) // 2 + 2 * (button_height + button_margin), resize_img,
                                  button_scale)
    picture_button = button.Button(width + button_margin,
                                   (height - total_button_height) // 2 + 3 * (button_height + button_margin), picture_img,
                                   button_scale)
    menu_button = button.Button(width + button_margin,
                                (height - total_button_height) // 2 + 4 * (button_height + button_margin), menu_img,
                                button_scale)


    font_size = int(22 * (scale_height + scale_width)/2)
    custom_font = pygame.font.Font("texturepack/RetroGaming.ttf", font_size)

    black = (0, 0, 0)
    white = (200, 200, 200)
    grey = (50, 50, 50)
    yellow = (204, 204, 0)


    matrix = numpy.empty((N, N), dtype=Grain)
    for i in range(N):
        for j in range(N):
            matrix[i, j] = Grain()

    for i in range(N):
        for j in range(N):
            matrix[i, j].val = 1 if initial_board[i, j] == 1 else 0


    for i in range(N - 1):
        for j in range(N - 2):
            matrix[i, j + 1].left = matrix[i + 1, j - 1 + 1]
            matrix[i, j + 1].center = matrix[i + 1, j + 1]
            matrix[i, j + 1].right = matrix[i + 1, j + 1 + 1]



    all_sand = []
    for i in range(N):
        for j in range(N):
            if matrix[i, j].val == 1:
                all_sand.append(matrix[i, j])

    all_sand = new_alive_list(matrix, N)

    drawing = False

    continuos_sim = 0
    tick = 60
    press = 0

    clear_area_rect = pygame.Rect(width, 0, button_window_width, height)
    pygame.draw.rect(window, grey, clear_area_rect)

    text_space = custom_font.render("Press SPACE to", True, yellow)
    text_space2 = custom_font.render("perform next step", True, yellow)

    text_space_rect = text_space.get_rect(
        topleft=(
            width + button_margin, button_margin * 2))

    text_space2_rect = text_space2.get_rect(
        topleft=(
            width + button_margin, button_margin * 4))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 0 < x < width and height > y > 0:
                        drawing = True
                        col = x // cell_size
                        row = y // cell_size
                        matrix[row, col].val = - matrix[row, col].val + 1
                        all_sand.append(matrix[row, col])
                        #print(matrix[row, col])
                        all_sand = new_alive_list(matrix, N)  # cos

            elif event.type == pygame.MOUSEMOTION and drawing:
                x, y = event.pos
                if 0 < x < width and height > y > 0:
                    col = x // cell_size
                    row = y // cell_size
                    matrix[row, col].val = - matrix[row, col].val + 1
                    all_sand.append(matrix[row, col])
                    all_sand = new_alive_list(matrix, N)  # cos

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                all_sand = let_them_fall3(all_sand)

            if simulation_button.draw(window) or (event.type == pygame.KEYDOWN and event.key == pygame.K_F10):
                continuos_sim = - continuos_sim + 1

            if reset_button.draw(window) or (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                for i in range(N):
                    for j in range(N):
                        matrix[i, j].val = 0
                all_sand = new_alive_list(matrix, N)  # cos

            if resize_button.draw(window):


                new_cell_size = askinteger("Resize", "Enter new cell size:")
                new_N = askinteger("Resize", "Enter new number of cells:")
                original_width, original_height = 700, 700
                new_width, new_height = new_N * new_cell_size, new_N * new_cell_size
                scale_width = new_width/original_width
                scale_height = new_height/original_height
                pygame.quit()
                sand_simulation(new_N, new_cell_size, scale_width, scale_height)
                # scale = (scale_width + scale_heigth)/2
                # print(N)
                # print(cell_size)
                # N = int(N * scale)
                # cell_size = int(cell_size * scale)
                # if N % cell_size == 0:
                #     sand_simulation(N,cell_size, scale)
                # else:
                #     N = N + N % cell_size
                #     sand_simulation(N,cell_size, scale)
                # print('---------------------')
                # print(N)
                # print(cell_size)




            if picture_button.draw(window):
                generation_count = 0
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename(title="Choose a photo",
                                                       filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                if file_path:
                    initial_board = black_and_white(file_path, N)
                    for i in range(N):
                        for j in range(N):
                            matrix[i, j].val = 1 if initial_board[i, j] == 1 else 0
                    for i in range(N):
                        for j in range(N):
                            if matrix[i, j].val == 1:
                                all_sand.append(matrix[i, j])

            if menu_button.draw(window):
                return

        if continuos_sim == 1:
            all_sand = let_them_fall3(all_sand)

        game_area.fill(black)

        for i in range(N):
            for j in range(N):
                if matrix[i, j].val == 1:
                    rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                    pygame.draw.rect(game_area, yellow, rect)

        for i in range(N + 1):
            pygame.draw.line(game_area, grey, (i * cell_size, 0), (i * cell_size, height), 1)
            pygame.draw.line(game_area, grey, (0, i * cell_size), (width, i * cell_size), 1)

        text_vanish = custom_font.render(f'Press on sand,', True, yellow)
        text_vanish2 = custom_font.render(f'it will vanish', True, yellow)

        # Adjust positions based on button placement
        text_vanish_rect = text_vanish.get_rect(
            topleft=(width + button_margin, (height - total_button_height) // 2 + total_button_height))
        text_vanish2_rect = text_vanish2.get_rect(
            topleft=(width + button_margin,
                     (height - total_button_height) // 2 + total_button_height + button_height + button_margin))

        window.blit(text_space, text_space_rect)
        window.blit(text_space2, text_space2_rect)

        window.blit(text_vanish, text_vanish_rect)
        window.blit(text_vanish2, text_vanish2_rect)


        pygame.display.flip()
        pygame.time.Clock().tick(tick)


#sand_simulation(100,7,1, 1)

