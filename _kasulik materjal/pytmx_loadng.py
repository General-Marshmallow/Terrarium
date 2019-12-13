import sys
import pygame
import pytmx
pygame.init()
window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
tmxdata = pytmx.TiledMap("maptest.tmx")
mapsize = tmxdata.width, tmxdata.height
tilesize = 40
blittablelist = []
rectlist = []


def get_texture(name):
    texture = pygame.transform.scale((pygame.image.load(name)), (tilesize, tilesize))
    return texture


def create_lists():
    global blittablelist, rectlist
    for yy in range(mapsize[1]):
        for xx in range(mapsize[0]):
            img = tmxdata.get_tile_image(xx, yy, 0)
            if img is None:
                pass
            else:
                rect = (xx * tilesize + 250, yy * tilesize, tilesize, tilesize)
                rectlist.append(rect)
                blittablerect = get_texture(img[0]), rect
                blittablelist.append(blittablerect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
    create_lists()
    screen.blits(blittablelist)
    blittablelist.clear()
    pygame.display.flip()
    clock.tick(60)
