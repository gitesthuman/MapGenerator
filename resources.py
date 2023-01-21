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

# rock = cv.imread("assets/rock_tileable.png")
# rock = cv.resize(rock, dim, interpolation=cv.INTER_AREA)
#
# wood = cv.imread("assets/wood_planks_tileable.png")
# wood = cv.resize(wood, dim, interpolation=cv.INTER_AREA)
#
# moss = cv.imread("assets/moss_tileable.png")
# moss = cv.resize(moss, dim, interpolation=cv.INTER_AREA)
#
# stone_bricks = cv.imread("assets/stone_bricks_tileable.png")
# stone_bricks = cv.resize(stone_bricks, dim, interpolation=cv.INTER_AREA)
#
# smooth_stone = cv.imread("assets/smooth_stone_tileable.png")
# smooth_stone = cv.resize(smooth_stone, dim, interpolation=cv.INTER_AREA)
#
# dark_smooth_stone = cv.imread("assets/dark_smooth_stone_tileable.png")
# dark_smooth_stone = cv.resize(dark_smooth_stone, dim, interpolation=cv.INTER_AREA)
#
# dark_smooth_stone_puddle = cv.imread("assets/dark_smooth_stone_with_puddle_tileable.png")
# dark_smooth_stone_puddle = cv.resize(dark_smooth_stone_puddle, dim, interpolation=cv.INTER_AREA)

# tile_mapper = {
#     "Wood": wood,
#     "Rock": rock,
#     "Moss": moss,
#     "Stone bricks": stone_bricks,
#     "Smooth stone": smooth_stone,
#     "Dark smooth stone": dark_smooth_stone,
#     "Dark smooth stone with puddle": dark_smooth_stone_puddle
# }
