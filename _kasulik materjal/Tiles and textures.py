import pygame
import sys
import random
import math
# from random import randint

pygame.init()
window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
background = 100, 100, 100
red = 255, 0, 0
white = 255, 255, 255
black = 0, 0, 0
green = 0, 100, 0
blue = 50, 50, 200
space = False
left = False
right = False
up = False
down = False
w = False
a = False
s = False
d = False
scrolling = False
x = 600
y = 300
i = 0
scrollspeed = 7
offset = [173, -3]
grid_length = 16
tilesize = 50
walkcount = 0
grid = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
        3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
        3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]


walk = [pygame.transform.scale(pygame.image.load('walk1.png'), (tilesize, tilesize)),
        pygame.transform.scale(pygame.image.load('walk2.png'), (tilesize, tilesize)),
        pygame.transform.scale(pygame.image.load('walk3.png'), (tilesize, tilesize)),
        pygame.transform.scale(pygame.image.load('walk4.png'), (tilesize, tilesize))]
collidable_blocks = pygame.sprite.Group


def refreshmap():
    tile_x = 0
    row = 0
    screen.fill(background)
    for x in grid:
        if x == 0:
            tilecolor = pygame.image.load("sky.png")
        elif x == 1:
            tilecolor = pygame.image.load("grass.png")
        elif x == 2:
            tilecolor = pygame.image.load("dirt.png")
        elif x == 3:
            tilecolor = pygame.image.load("stone.png")
        tilecolor = pygame.transform.scale(tilecolor, (tilesize, tilesize))
        if tile_x == grid_length:
            row += 1
            tile_x = 0
        if row > grid_length:
            row = 0
        if not x == 0:
            collidable_blocks.add(collidable_blocks)
        screen.blit(tilecolor, (tile_x * tilesize + offset[0], row * tilesize + offset[1]))
        tile_x += 1


def drawWindow():
    global walkcount
    refreshmap()
    if walkcount + 1 > 16:
        walkcount = 0
    if a or d:
        screen.blit(walk[walkcount//4], (x, y))
        walkcount += 1
    else:
        screen.blit(pygame.transform.scale(pygame.image.load('still.png'), (tilesize, tilesize)), (x, y))
    pygame.display.flip()
    clock.tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space = True
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            space = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            right = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            left = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            up = True
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            up = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            down = True
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            down = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            w = True
            walkcount = 0
            a = False
            d = False
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            w = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            a = True
            d = False
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            a = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            s = True
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            s = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            d = True
            a = False
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            d = False

    if scrolling:
        if left:
            offset[0] += scrollspeed
        if right:
            offset[0] -= scrollspeed
        if up:
            offset[1] += scrollspeed
        if down:
            offset[1] -= scrollspeed

    print(collidable_blocks)
    # DrawCycle
    drawWindow()
