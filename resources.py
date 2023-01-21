import cv2 as cv


square_size = 50
dim = (square_size, square_size)

rock = cv.imread("assets/rock_tileable.png")
rock = cv.resize(rock, dim, interpolation=cv.INTER_AREA)

wood = cv.imread("assets/wood_planks_tileable.png")
wood = cv.resize(wood, dim, interpolation=cv.INTER_AREA)

moss = cv.imread("assets/moss_tileable.png")
moss = cv.resize(moss, dim, interpolation=cv.INTER_AREA)

stone_bricks = cv.imread("assets/stone_bricks_tileable.png")
stone_bricks = cv.resize(stone_bricks, dim, interpolation=cv.INTER_AREA)

smooth_stone = cv.imread("assets/smooth_stone_tileable.png")
smooth_stone = cv.resize(smooth_stone, dim, interpolation=cv.INTER_AREA)

dark_smooth_stone = cv.imread("assets/dark_smooth_stone_tileable.png")
dark_smooth_stone = cv.resize(dark_smooth_stone, dim, interpolation=cv.INTER_AREA)

dark_smooth_stone_puddle = cv.imread("assets/dark_smooth_stone_with_puddle_tileable.png")
dark_smooth_stone_puddle = cv.resize(dark_smooth_stone_puddle, dim, interpolation=cv.INTER_AREA)


tile_mapper = {
    "Wood": wood,
    "Rock": rock,
    "Moss": moss,
    "Stone bricks": stone_bricks,
    "Smooth stone": smooth_stone,
    "Dark smooth stone": dark_smooth_stone,
    "Dark smooth stone with puddle": dark_smooth_stone_puddle
}
