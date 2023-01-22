import cv2 as cv


def scale_images(square_size):
    dim = (square_size, square_size)

    for t in textures:
        img = cv.imread(t[0])
        img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        tile_mapper[t[1]] = img


textures = [
    ("assets/rock_tileable.png", "Rock"),
    ("assets/wood_planks_tileable.png", "Wood"),
    ("assets/moss_tileable.png", "Moss"),
    ("assets/stone_bricks_tileable.png", "Stone bricks"),
    ("assets/smooth_stone_tileable.png", "Smooth stone"),
    ("assets/dark_smooth_stone_tileable.png", "Dark smooth stone"),
    ("assets/dark_smooth_stone_with_puddle_tileable.png", "Dark smooth stone with puddle")
]
tile_mapper = dict()
