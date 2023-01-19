import numpy as np
import matplotlib.pyplot as plt
import os

from resources import *


margin = 100

game_map = None
accept = False
end = False
while not accept and not end:
    file_name = input("Enter your file's path: ")

    if not os.path.isfile(file_name):
        print("File not found.")
        continue

    tiles = []
    for row in open(file_name, "r").read().splitlines():
        tiles.append(row.split(";"))

    w = len(tiles[0])
    h = len(tiles)

    game_map = np.zeros((2 * margin + w * square_size, 2 * margin + h * square_size, 3), np.uint8)

    for x, row in enumerate(tiles):
        for y, tile in enumerate(row):
            if tile in tile_mapper:
                game_map[margin + x * square_size:margin + (x + 1) * square_size,
                         margin + y * square_size:margin + (y + 1) * square_size] = tile_mapper[tile]

    plt.imshow(cv.merge(list(reversed(cv.split(game_map)))))
    plt.show()
    accept = input("Is this what you want your map to look like? (type yes/no) ") == "yes"
    if not accept:
        end = input("Do you want to try again? (type yes/no) ") == "no"

if accept:
    cv.imwrite("your_map.png", game_map)
    print("File saved as \"your_map.png\"")
