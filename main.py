import pygame
import data.constants as dc

pygame.init()

display = pygame.display.set_mode((
    dc.DISPLAY_WIDTH,
    dc.DISPLAY_HEIGHT,
))
screen = pygame.Surface((
    dc.SCREEN_WIDTH,
    dc.SCREEN_HEIGHT,
))
pygame.display.set_caption('Richochet Robots')

# gear A
# star B
# moon C
# planet D
# (ix, iy): (symb_color, symb_symbol)
board_symbols = {
    (2, 1): (dc.COLOR_GREEN, 'a'),
    (1, 6): (dc.COLOR_YELLOW, 'b'),
    (1, 9): (dc.COLOR_GREEN, 'b'),
    (2, 14): (dc.COLOR_YELLOW, 'c'),
    (4, 10): (dc.COLOR_RED, 'd'),
    (5, 6): (dc.COLOR_BLUE, 'd')
}

mainClock = pygame.time.Clock()

def label(surf: pygame.Surface, symb: str, fg: tuple = None, bg: tuple = None):
    if bg is not None:
        screen.blit(dc.COLOR_SURFS[bg], (
            # symb[0]: symbol color
            ix * dc.TILE_WIDTH,
            iy * dc.TILE_HEIGHT,
        ))
    copy = dc.sprites[symb].copy()
    if fg is not None:
        copy.blit(dc.COLOR_SURFS[fg], (
            0, 0,
        ), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(copy, (
        ix * dc.TILE_WIDTH,
        iy * dc.TILE_HEIGHT,
    ))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    screen.fill(dc.COLOR_BLACK)

    for iy in range(dc.TILES_WIDE):
        for ix in range(dc.TILES_TALL):
            if (iy, ix) in board_symbols.keys():
                color, symb = board_symbols[(iy, ix)]
                label(surf=screen, symb=symb, fg=dc.COLOR_BLACK, bg=color)
            # elif:
            else:
                label(surf=screen, symb='.')

    pygame.transform.scale(
        screen,
        (
            dc.DISPLAY_WIDTH,
            dc.DISPLAY_HEIGHT,
        ),
        display,
    )

    pygame.display.update()
    mainClock.tick(dc.FPS)

pygame.quit()
