import matplotlib.pyplot as plt
import os
import numpy as np
import pygame
from tkinter import *

from resources import *


def make_form(rt, fds):
    ents = {}
    for field in fds:
        row = Frame(rt)
        lab = Label(row, width=10, text=field + ": ", anchor='w')
        ent = Entry(row)
        if field == "Width":
            ent.insert(0, 10)
        elif field == "Height":
            ent.insert(0, 10)
        elif field == "Square size":
            ent.insert(0, 50)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        ents[field] = ent
    return ents


def form_action():
    global confirm
    global root
    confirm = True
    root.quit()


def paste_image(src: np.ndarray, dest: np.ndarray, x_offset: int, y_offset: int):
    """
    pastes src on dest with x,y offsets
    :param src: source image
    :param dest: destination image
    :param x_offset: x offset in dest
    :param y_offset: y offset in dest
    """
    y1, y2 = y_offset, y_offset + src.shape[0]
    x1, x2 = x_offset, x_offset + src.shape[1]

    alpha_src = src[:, :, 3] / 255.0
    alpha_dest = 1.0 - alpha_src

    for c in range(0, 3):
        dest[y1:y2, x1:x2, c] = (alpha_src * src[:, :, c] + alpha_dest * dest[y1:y2, x1:x2, c])


confirm = False
fields = ('Width', 'Height', 'Square size')
root = Tk()
root.title("Map Generator")
entries = make_form(root, fields)
button1 = Button(root, text='Confirm', command=form_action)
button1.pack(side=BOTTOM, padx=5, pady=5)
root.mainloop()

if not confirm:
    exit(0)

width = int(entries['Width'].get())
height = int(entries['Height'].get())
square_size = int(entries['Square size'].get())

root.destroy()
pygame.init()
pygame.display.set_caption("Map Creator")
screen_width = width * square_size
screen_height = height * square_size
screen = pygame.display.set_mode((width * square_size, height * square_size))

small_font = pygame.font.SysFont('Arial', 12)
black = (0, 0, 0)
color_light = (176, 176, 176)
color_dark = (130, 130, 130)
hover_color = (255, 255, 255)
board_color = (143, 210, 255)
line_color = (194, 242, 252)

tiles = [[None for col in range(width)] for row in range(height)]
scale_images(square_size)

hover = pygame.Surface((square_size, square_size))
hover.set_alpha(75)
hover.fill(hover_color)

done = False
while not done:
    mouse = pygame.mouse.get_pos()
    screen.fill(board_color)

    for k in range(1, width):
        pygame.draw.rect(screen, line_color, pygame.Rect(k * square_size, 0, 2, screen_height))
    for k in range(1, height):
        pygame.draw.rect(screen, line_color, pygame.Rect(0, k * square_size, screen_width, 2))

    for j, row in enumerate(tiles):
        for i, t in enumerate(row):
            if t:
                screen.blit(pygame.image.frombuffer(tile_mapper[t].tobytes(), tile_mapper[t].shape[1::-1], "BGR"),
                            (square_size * i, square_size * j))

    screen.blit(hover, ((mouse[0] // square_size) * square_size, (mouse[1] // square_size) * square_size))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit(0)
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                done = True
                break
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 3:
            x = mouse[0] // square_size
            y = mouse[1] // square_size

            available_tiles = [(small_font.render(t, True, black), t) for t in tile_mapper]
            option_w = max([t[0].get_width() for t in available_tiles])
            option_h = 12

            posX = min(mouse[0], screen_width - option_w)
            posY = min(mouse[1], screen_height - option_h * len(available_tiles))

            added = False
            while not added:
                mouse = pygame.mouse.get_pos()

                for i, t in enumerate(available_tiles):
                    if posX <= mouse[0] < posX + option_w \
                            and posY + option_h * i <= mouse[1] < posY + option_h * (i + 1):
                        pygame.draw.rect(screen, color_light,
                                         pygame.Rect(posX, posY + option_h * i, option_w, option_h))
                    else:
                        pygame.draw.rect(screen, color_dark,
                                         pygame.Rect(posX, posY + option_h * i, option_w, option_h))

                for ev2 in pygame.event.get():
                    if ev2.type == pygame.QUIT:
                        sys.exit(0)
                    if ev2.type == pygame.MOUSEBUTTONDOWN and ev2.button == 1:
                        for i, t in enumerate(available_tiles):
                            if posX <= mouse[0] < posX + option_w \
                                    and posY + option_h * i <= mouse[1] < posY + option_h * (i + 1):
                                tiles[y][x] = t[1]
                                break

                        added = True

                for i, t in enumerate(available_tiles):
                    screen.blit(t[0], (posX, posY + option_h * i - 1))

                pygame.display.update()

    pygame.display.update()

game_map = np.zeros((screen_width, screen_height, 3), np.uint8)

for y, row in enumerate(tiles):
    for x, t in enumerate(row):
        if t in tile_mapper:
            game_map[y * square_size:(y + 1) * square_size,
                     x * square_size:(x + 1) * square_size, :] = tile_mapper[t][:, :, :]

cv.imwrite("your_map.png", game_map)
exit(0)
