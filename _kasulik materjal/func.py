import pygame
import sys
import pytmx
from main_fürher import *
from var import *
playertileset = pytmx.TiledTileset('player.tsx')


def get_texture(name):
    texture = pygame.transform.scale((pygame.image.load("textures/" + name)), (tilesize, tilesize))
    return texture


def collide(obj: pygame.Rect):
    obj = pygame.Rect(obj)
    collision_inn_x = False
    collision_inn_y = False
    hitonleft = False
    hitonright = False
    hitontop = False
    hitonbottom = False
    hb = hitbox
    # Check both sides for collision
    if obj.collidepoint(hb.left, hb[1]) and (
            obj.collidepoint(hb.topleft[0], hb.topleft[1]) or obj.collidepoint(hb.bottomleft[0], hb.bottomleft[1])):
        hitonleft = True
        collision_inn_x = True
    if obj.collidepoint(hb.right, hb[1]) and (
            obj.collidepoint(hb.topright[0], hb.topright[1]) or obj.collidepoint(hb.bottomright[0],
                                                                                 hb.bottomright[1])):
        hitonright = True
        collision_inn_x = True
    # If sides not colliding, check bottom collision
    if not collision_inn_x and (
            obj.collidepoint(hb.bottomleft[0], hb.bottomleft[1]) or obj.collidepoint(hb.bottomright[0],
                                                                                     hb.bottomleft[1])):
        hitonbottom = True
        collision_inn_y = True
    # If sides not colliding, check top collision
    if not collision_inn_x and (
            obj.collidepoint(hb.topleft[0], hb.topleft[1]) or obj.collidepoint(hb.topright[0], hb.topright[1])):
        hitontop = True
        collision_inn_y = True
        print(collision_inn_x, collision_inn_y, hitonleft, hitonright, hitontop, hitonbottom)
    return collision_inn_x, collision_inn_y, hitonleft, hitonright, hitontop, hitonbottom


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


def get_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()


def player_animation():
    global walkcount
    if walkcount + 1 > 16:
        walkcount = 0
    if a or d:
        blittableplayer = walkimg[walkcount // 4], player_screen_pos
        walkcount += 1
    elif jump:
        blittableplayer = jumpimg, player_screen_pos
    else:
        blittableplayer = stillimg, player_screen_pos


def render():
    global blittablelist, rectlist
    rectlist.clear()
    blittablelist.clear()
    for y in range(mapsize[1]):
        for x in range(mapsize[0]):
            img = tmxdata.get_tile_image(x, y, 0)
            if img is None:
                pass
            else:
                rect = (x * tilesize + offset, y * tilesize + offset, tilesize, tilesize)
                rectlist.append(rect)
                blittablerect = get_texture(img[0]), rect
                blittablelist.append(blittablerect)
