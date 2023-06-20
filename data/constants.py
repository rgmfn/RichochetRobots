import pygame

iota_ctr = 0
def iota(reset=False):
    global iota_ctr
    iota_ctr += 1
    if reset:
        iota_ctr = 0

    return iota_ctr

spritesheet = pygame.image.load('assets/MRMOTEXT EX.png')
SPRITES_PER_ROW = 32

TILE_WIDTH = 8
TILE_HEIGHT = 8

SCALE = 6

TILES_WIDE = 16
TILES_TALL = 16

SCREEN_WIDTH = TILE_WIDTH * TILES_WIDE
SCREEN_HEIGHT = TILE_HEIGHT * TILES_TALL

DISPLAY_WIDTH = SCREEN_WIDTH * SCALE
DISPLAY_HEIGHT = SCREEN_HEIGHT * SCALE

FPS = 30

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GRAY = (100, 100, 100)
COLOR_WHITE = (255, 255, 255)
COLOR_PINK = (255, 0, 255)

sprites = {}
for ch in range(ord('a'), ord('z')+1):
    pos = 897 + (ch - ord('a'))
    sprites[chr(ch)] = spritesheet.subsurface((
        (pos % SPRITES_PER_ROW) * TILE_WIDTH,
        (pos // SPRITES_PER_ROW) * TILE_HEIGHT,
        TILE_WIDTH,
        TILE_HEIGHT,
    ))
for ch in range(ord('0'), ord('9')+1):
    pos = 880 + (ch - ord('0'))
    sprites[chr(ch)] = spritesheet.subsurface((
        (pos % SPRITES_PER_ROW) * TILE_WIDTH,
        (pos // SPRITES_PER_ROW) * TILE_HEIGHT,
        TILE_WIDTH,
        TILE_HEIGHT,
    ))
sprites['dot'] = spritesheet.subsurface((
    (439 % SPRITES_PER_ROW) * TILE_WIDTH,
    (439 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['.'] = spritesheet.subsurface((
    (878 % SPRITES_PER_ROW) * TILE_WIDTH,
    (878 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['.'] = spritesheet.subsurface((
    (878 % SPRITES_PER_ROW) * TILE_WIDTH,
    (878 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['left'] = spritesheet.subsurface((
    (57 % SPRITES_PER_ROW) * TILE_WIDTH,
    (57 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['right'] = spritesheet.subsurface((
    (59 % SPRITES_PER_ROW) * TILE_WIDTH,
    (59 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['top'] = spritesheet.subsurface((
    (26 % SPRITES_PER_ROW) * TILE_WIDTH,
    (26 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['bottom'] = spritesheet.subsurface((
    (90 % SPRITES_PER_ROW) * TILE_WIDTH,
    (90 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['top left'] = spritesheet.subsurface((
    (530 % SPRITES_PER_ROW) * TILE_WIDTH,
    (530 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['top right'] = spritesheet.subsurface((
    (531 % SPRITES_PER_ROW) * TILE_WIDTH,
    (531 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['bottom left'] = spritesheet.subsurface((
    (562 % SPRITES_PER_ROW) * TILE_WIDTH,
    (562 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
sprites['bottom right'] = spritesheet.subsurface((
    (563 % SPRITES_PER_ROW) * TILE_WIDTH,
    (563 // SPRITES_PER_ROW) * TILE_HEIGHT,
    TILE_WIDTH,
    TILE_HEIGHT,
))
for sprite in sprites.values():
    sprite.set_colorkey(COLOR_BLACK)

base_surface = pygame.Surface((
    TILE_WIDTH,
    TILE_HEIGHT,
))
COLORS = [
    COLOR_BLUE, 
    COLOR_GRAY,
    COLOR_GREEN,
    COLOR_RED,
    COLOR_YELLOW,
    COLOR_BLACK,
    COLOR_WHITE,
    COLOR_PINK,
]
COLOR_SURFS = {}
for color in COLORS:
    surf = base_surface.copy()
    surf.fill(color)
    COLOR_SURFS[color] = surf
