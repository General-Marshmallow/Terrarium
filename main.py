import pytmx
import pygame
import sys
pygame.init()
window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

tilesize = 50
mapchanged = False


class Player:
    def __init__(self):
        self.hitbox = 50, 50
        self.loc = [0, 0]


def get_texture(texture_name):
    addr = "textures/" + texture_name
    texture = pygame.transform.scale(pygame.image.load(addr), (tilesize, tilesize))
    return texture


def get_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()


while True:

    get_event()
    clock.tick(60)
