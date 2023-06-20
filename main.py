import pygame
import random
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

# robot_pos: {[y, x]}
robot_pos = {
    YELLOW: (1, 1),
    GREEN: (3, 3),
    RED: (5, 5),
    BLUE: (12, 12),
    GRAY: (10, 10),
}
ROBOT_COLORS = {
    YELLOW: dc.COLOR_YELLOW,
    GREEN: dc.COLOR_GREEN,
    RED: dc.COLOR_RED,
    BLUE: dc.COLOR_BLUE,
    GRAY: dc.COLOR_GRAY,
}
sel_robot: int = -1

def move(dx: int = 0, dy: int = 0):
    global robot_pos, sel_robot
    is_moving: bool = True

    while is_moving:
        curr_pos: tuple = robot_pos[sel_robot]
        next_pos: tuple = (robot_pos[sel_robot][0]+dy, robot_pos[sel_robot][1]+dx)
        if curr_pos in walls.keys():
            if dx == -1 and walls[curr_pos] == 'left':
                is_moving = False
            elif dx == 1 and walls[curr_pos] == 'right':
                is_moving = False
            elif dy == -1 and walls[curr_pos] == 'top':
                is_moving = False
            elif dy == 1 and walls[curr_pos] == 'bottom':
                is_moving = False
        if next_pos in walls.keys():
            if dx == -1 and walls[next_pos] == 'right':
                is_moving = False
            elif dx == 1 and walls[next_pos] == 'left':
                is_moving = False
            elif dy == -1 and walls[next_pos] == 'bottom':
                is_moving = False
            elif dy == 1 and walls[next_pos] == 'top':
                is_moving = False
        if not 0 <= next_pos[0] < 16:
            is_moving = False
        elif not 0 <= next_pos[1] < 16:
            is_moving = False
        if next_pos in robot_pos.values():
            is_moving = False
        if 7 <= next_pos[0] <= 8 and 7 <= next_pos[1] <= 8:
            is_moving = False

        if is_moving:
            robot_pos[sel_robot] = (
                robot_pos[sel_robot][0] + dy,
                robot_pos[sel_robot][1] + dx
            )
            # print(robot_pos[sel_robot])

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

print(random.choice(list(dests.values())))

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
                move(dy=-1)
            elif event.key == pygame.K_DOWN:
                move(dy=1)
            elif event.key == pygame.K_LEFT:
                move(dx=-1)
            elif event.key == pygame.K_RIGHT:
                move(dx=1)
    
    screen.fill(dc.COLOR_BLACK)

    for iy in range(dc.TILES_WIDE):
        for ix in range(dc.TILES_TALL):
            if 7 <= iy <= 8 and 7 <= ix <= 8:
                label(surf=screen, symb='a', fg=dc.COLOR_BLACK)
                continue

            drew_robot = False
            for robot_num in range(1, 5+1):
                if (iy, ix) == robot_pos[robot_num]:
                    bg = dc.COLOR_PINK if sel_robot == robot_num else None
                    label(surf=screen, symb=str(robot_num), fg=ROBOT_COLORS[robot_num], bg=bg)
                    drew_robot = True

            if drew_robot:
                if (iy, ix) in walls.keys():
                    symb = walls[(iy, ix)]
                    label(surf=screen, symb=symb)
                continue

            if (iy, ix) in dests.keys():
                color, symb = dests[(iy, ix)]
                label(surf=screen, symb=symb, fg=dc.COLOR_BLACK, bg=color)
            else:
                if (iy, ix) in walls.keys():
                    symb = walls[(iy, ix)]
                    label(surf=screen, symb=symb)

                label(surf=screen, symb='dot')

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
