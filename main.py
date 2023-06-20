import pygame
import data.constants as dc
import data.map as dm

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

YELLOW = dc.iota()
GREEN = dc.iota()
RED = dc.iota()
BLUE = dc.iota()
GRAY = dc.iota()

robot_pos = {
    YELLOW: [1, 1],
    GREEN: [3, 3],
    RED: [5, 5],
    BLUE: [7, 7],
    GRAY: [10, 10],
}
ROBOT_COLORS = {
    YELLOW: dc.COLOR_YELLOW,
    GREEN: dc.COLOR_GREEN,
    RED: dc.COLOR_RED,
    BLUE: dc.COLOR_BLUE,
    GRAY: dc.COLOR_GRAY,
}
sel_robot: int = -1

# dests {(iy, ix): (dest_color, dest_symbol)}
# walls [(iy, ix): wall_symbol]
dests, walls = dm.load_map('map.txt')
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
            elif event.key == pygame.K_1:
                sel_robot = YELLOW
            elif event.key == pygame.K_2:
                sel_robot = GREEN
            elif event.key == pygame.K_3:
                sel_robot = RED
            elif event.key == pygame.K_4:
                sel_robot = BLUE
            elif event.key == pygame.K_5:
                sel_robot = GRAY
            elif event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
            elif event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
    
    screen.fill(dc.COLOR_BLACK)

    for iy in range(dc.TILES_WIDE):
        for ix in range(dc.TILES_TALL):
            for robot_num in range(1, 5+1):
                if (iy, ix) == robot_pos[robot_num]:
                    label(surf=screen, symb=str(robot_num), fg=ROBOT_COLORS[robot_num])
                    continue

            if (iy, ix) in dests.keys():
                color, symb = dests[(iy, ix)]
                label(surf=screen, symb=symb, fg=dc.COLOR_BLACK, bg=color)
            else:
                if (iy, ix) in walls.keys():
                    symb = walls[(iy, ix)]
                    label(surf=screen, symb=symb)

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
