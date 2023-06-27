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

MVT_KEYS = {
    pygame.K_UP: (0, -1),
    pygame.K_w: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_s: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_a: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_d: (1, 0),
}

# robot_pos: {[y, x]}
robot_pos = {
    dc.YELLOW: (1, 1),
    dc.GREEN: (3, 3),
    dc.RED: (5, 5),
    dc.BLUE: (12, 12),
    dc.GRAY: (10, 10),
}
ROBOT_COLORS = {
    dc.YELLOW: dc.COLOR_YELLOW,
    dc.GREEN: dc.COLOR_GREEN,
    dc.RED: dc.COLOR_RED,
    dc.BLUE: dc.COLOR_BLUE,
    dc.GRAY: dc.COLOR_GRAY,
}
sel_robot: int = -1

def move(dx: int = 0, dy: int = 0):
    global robot_pos, sel_robot
    init_pos = robot_pos[sel_robot]
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

    if init_pos == robot_pos[sel_robot]:
        return 0
    else:
        return 1

# dests {(iy, ix): (dest_color, dest_symbol)}
# walls [(iy, ix): wall_symbol]
dests, walls = dm.load_map('map.txt')
possible_dests: list = list(dests.keys())
exit = random.choice(list(dests.keys()))
possible_dests.remove(exit)

mainClock = pygame.time.Clock()

def label(surf: pygame.Surface, pos: tuple, symb: str = None, word: str = None, fg: tuple = None, bg: tuple = None):
    """
        pos: (y, x)
    """
    if word is not None:
        for i, s in enumerate(word):
            label(surf=surf, pos=(pos[0], pos[1]+i), symb=word[i], fg=fg, bg=bg)
        return

    iy, ix = pos
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

moves = 0

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_1:
                sel_robot = dc.YELLOW
            elif event.key == pygame.K_2:
                sel_robot = dc.GREEN
            elif event.key == pygame.K_3:
                sel_robot = dc.RED
            elif event.key == pygame.K_4:
                sel_robot = dc.BLUE
            elif event.key == pygame.K_5:
                sel_robot = dc.GRAY
            elif event.key in MVT_KEYS:
                moves += move(dx=MVT_KEYS[event.key][0], dy=MVT_KEYS[event.key][1])

            if robot_pos[dests[exit][0]] == exit:
                # TODO pull out into method?
                # go to next turn
                if len(possible_dests) > 0:
                    exit = random.choice(possible_dests)
                    possible_dests.remove(exit)
                    moves = 0
                else:
                    run = False
    
    screen.fill(dc.COLOR_BLACK)

    for iy in range(dc.TILES_WIDE):
        for ix in range(dc.TILES_TALL):
            if 7 <= iy <= 8 and 7 <= ix <= 8:
                label(surf=screen, pos=(iy, ix), symb='a', fg=dc.COLOR_BLACK)
                continue

            drew_robot = False
            for robot_num in range(1, 5+1):
                if (iy, ix) == robot_pos[robot_num]:
                    bg = dc.COLOR_PINK if sel_robot == robot_num else None
                    label(surf=screen, pos=(iy, ix), symb=str(robot_num), fg=ROBOT_COLORS[robot_num], bg=bg)
                    drew_robot = True

            if drew_robot:
                if (iy, ix) in walls.keys():
                    symb = walls[(iy, ix)]
                    label(surf=screen, pos=(iy, ix), symb=symb)
                continue

            if (iy, ix) in dests.keys():
                color, symb = dests[(iy, ix)]
                label(surf=screen, pos=(iy, ix), symb=symb, fg=dc.COLOR_BLACK, bg=ROBOT_COLORS[color])
            else:
                label(surf=screen, pos=(iy, ix), symb='square', fg=dc.COLOR_LGRAY)

                if (iy, ix) in walls.keys():
                    symb = walls[(iy, ix)]
                    label(surf=screen, pos=(iy, ix), symb=symb)

    label(surf=screen, pos=(dc.TILES_TALL+dc.HUD_TILES_TALL-1, 0), symb=dests[exit][1], fg=dc.COLOR_BLACK, bg=ROBOT_COLORS[dests[exit][0]])

    label(surf=screen, pos=(dc.TILES_TALL+dc.HUD_TILES_TALL-1, 2), word=str(moves), fg=dc.COLOR_FG)

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
