import pygame

pygame.init

pacman_images = {
    'up': pygame.image.load('resours/pacman_up.png'),
    'down': pygame.image.load('resours/pacman_down.png'),
    'left': pygame.image.load('resours/pacman_left.png'),
    'right': pygame.image.load('resours/pacman_right.png'),
    'up_left': pygame.image.load('resours/pacman_up_left.png'),
    'up_right': pygame.image.load('resours/pacman_up_right.png'),
    'down_left': pygame.image.load('resours/pacman_down_left.png'),
    'down_right': pygame.image.load('resours/pacman_down_right.png')
}


def get_direction(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    direction = 'right'

    if dy < 0:
        if dx < 0:
            direction = 'up_left'
        elif dx > 0:
            direction = 'up_right'
        else:
            direction = 'up'
    elif dy > 0:
        if dx < 0:
            direction = 'down_left'
        elif dx > 0:
            direction = 'down_right'
        else:
            direction = 'down'
    else:
        if dx < 0:
            direction = 'left'
        elif dx > 0:
            direction = 'right'

    return direction

def move_towards(pos1, pos2, speed):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > speed:
        x1 += speed if dx > 0 else -speed
    else:
        x1 = x2

    if abs(dy) > speed:
        y1 += speed if dy > 0 else -speed
    else:
        y1 = y2

    return (x1, y1)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pac-man смотрит на курсор')

BACKGROUND = (0, 0, 0)

pacman_pos = (400, 300)
speed = 4

clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    for event in pygame.event.get():
        if event.type