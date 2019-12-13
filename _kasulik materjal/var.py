import pygame
import sys
import pytmx

window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
space = False
jump = False
left = False
right = False
up = False
down = False
w = False
a = False
s = False
d = False
scrolling = False
i = 0
walkcount = 0
offset = [350, 100]
tilesize = 40
walkcount = 0
player_screen_pos = player_screen_pos_x, player_screen_pos_y = window_width / 2 - tilesize / 2, window_height / 2 - tilesize / 2
jumpingvariable = 50
movementspeed = 15
velocity = [0, 0]
collideaddr = 0
y_ax_collision_thing = 5

tiles = []
collidedtile = []
player = ()
hitbox = pygame.Rect(player_screen_pos, (tilesize, tilesize))
# background = pygame.transform.scale(pygame.image.load('background.jpg').convert(), window_size)
# font = pygame.font.Font(None, 30)
tmxdata = pytmx.TiledMap("maptest.tmx")
mapsize = tmxdata.width, tmxdata.height
tilesize = 40
blittablelist = []
rectlist = []