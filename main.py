import matplotlib.pyplot as plt
import os
import numpy as np
import pygame
from tkinter import *

from resources import *


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=10, text=field + ": ", anchor='w')
        ent = Entry(row)
        if field == "Width":
            ent.insert(0, width)
        elif field == "Height":
            ent.insert(0, height)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def form_action():
    global go
    global root
    go = True
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


go = False
width = 10
height = 10
fields = ('Width', 'Height')
root = Tk()
root.title("Map Generator")
entries = makeform(root, fields)
# root.bind('<Return>', (lambda event, e=entries: fetch(e)))
button1 = Button(root, text='Confirm', command=form_action)
button1.pack(side=BOTTOM, padx=5, pady=5)
root.mainloop()

if go:
    width = int(entries['Width'].get())
    height = int(entries['Height'].get())
else:
    exit(0)

root.destroy()
pygame.init()
pygame.display.set_caption("Map Creator")
screen_width = width * square_size
screen_height = height * square_size
screen = pygame.display.set_mode((width * square_size, height * square_size))

tiles = [[None for col in range(width)] for row in range(height)]

done = False
while not done:
    mouse = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    for j, row in enumerate(tiles):
        for i, t in enumerate(row):
            if t:
                screen.blit(pygame.image.frombuffer(tile_mapper[t].tobytes(), tile_mapper[t].shape[1::-1], "BGR"),
                            (square_size * i, square_size * j))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit(0)
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                done = True
                break
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button in [1, 3]:
            x = (mouse[0] - screen_width) // square_size
            y = (mouse[1] - screen_height) // square_size

            posX = mouse[0]
            posY = mouse[1]
            added = False
            black = (0, 0, 0)
            small_font = pygame.font.SysFont('Arial', 12)
            color_light = (176, 176, 176)
            color_dark = (130, 130, 130)

            available_tiles = [(small_font.render(t, True, black), t) for t in tile_mapper]

            while not added:
                mouse = pygame.mouse.get_pos()

                option_w = max([t[0].get_width() for t in available_tiles])
                option_h = 12

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
                    if ev2.type == pygame.MOUSEBUTTONDOWN and ev2.button == 1:  # dodanie (rzeczywiste kliknięcie)
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
            # paste_image(tile_mapper[t], game_map, x * square_size, y * square_size)

cv.imwrite("your_map.png", game_map)
sys.exit(0)

# margin = 100
#
# game_map = None
# accept = False
# end = False
# while not accept and not end:
#     file_name = input("Enter your file's path: ")
#
#     if not os.path.isfile(file_name):
#         print("File not found.")
#         continue
#
#     tiles = []
#     for row in open(file_name, "r").read().splitlines():
#         tiles.append(row.split(";"))
#
#     w = len(tiles[0])
#     h = len(tiles)
#
#     game_map = np.zeros((2 * margin + w * square_size, 2 * margin + h * square_size, 3), np.uint8)
#
#     for x, row in enumerate(tiles):
#         for y, tile in enumerate(row):
#             if tile in tile_mapper:
#                 game_map[margin + x * square_size:margin + (x + 1) * square_size,
#                          margin + y * square_size:margin + (y + 1) * square_size] = tile_mapper[tile]
#
#     plt.imshow(cv.merge(list(reversed(cv.split(game_map)))))
#     plt.show()
#     accept = input("Is this what you want your map to look like? (type yes/no) ") == "yes"
#     if not accept:
#         end = input("Do you want to try again? (type yes/no) ") == "no"
#
# if accept:
#     cv.imwrite("your_map.png", game_map)
#     print("File saved as \"your_map.png\"")
