import pytmx, pygame, sys

pygame.init()
window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

blittablelist = []
rectlist = []
offset = [0, 200]
tilesize = 30
mapchanged = False
tmxdata = pytmx.TiledMap("textures/map.tmx")
layerlist = tmxdata.layers
print(layerlist)


def get_texture(texture_name):
    # addr = "textures/" + texture_name
    texture = pygame.transform.scale(pygame.image.load(texture_name), (tilesize, tilesize))
    return texture


def create_lists():
    global blittablelist, rectlist, offset
    rectlist.clear()
    blittablelist.clear()
    for n in range(len(tmxdata.layers)):
        for yy in range(tmxdata.height):
            for xx in range(tmxdata.width):
                img = tmxdata.get_tile_image(xx, yy, n)
                if img is None:
                    pass
                else:
                    rect = (xx * tilesize - offset[0], yy * tilesize - offset[1], tilesize, tilesize)
                    blittablerect = get_texture(img[0]), rect
                    blittablelist.append(blittablerect)
                    #print(layerlist)
                    #print(layerlist[n])
                    if n == 2:
                        rectlist.append(rect)
    print(rectlist)


class Event:
    w = False
    a = False
    s = False
    d = False
    last_dir = "a"
    space = False
    mouse_pos = []
    left_click = False
    right_click = False

    def get_event(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.space = True
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                self.space = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
                self.w = True
            if e.type == pygame.KEYUP and e.key == pygame.K_w:
                self.w = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
                self.a = True
                self.d = False
                self.last_dir = "a"
            if e.type == pygame.KEYUP and e.key == pygame.K_a:
                self.a = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
                self.s = True
            if e.type == pygame.KEYUP and e.key == pygame.K_s:
                self.s = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
                self.d = True
                self.a = False
                self.last_dir = "d"
            if e.type == pygame.KEYUP and e.key == pygame.K_d:
                self.d = False


event = Event()


class Player:
    screen_location = (window_width / 2 - tilesize / 2, window_height / 2 - tilesize / 2)
    walknames = ["textures/walk1.png", "textures/walk2.png", "textures/walk3.png", "textures/walk3.png", "textures/walk4.png", "textures/walk5.png", "textures/walk6.png"]
    stillname = "textures/still.png"
    jumpname = "textures/jump.png"
    hitbox = (tilesize, tilesize)
    walkcount = 0
    jumpcount = 0
    velocity = [0, 0]
    location = [window_width / 2 - tilesize / 2, window_height / 2 - tilesize / 2]
    oofset = []
    movingspeed = 15
    deceleration = 2
    jumpspeed = 50
    gravity_strength = 2  # pixels per second every second
    jumping = False

    def __init__(self):
        self.oofset = offset

    def get_player_frame(self):
        if self.walkcount + 1 > 18:
            self.walkcount = 0
        # If still and which direction
        if not (event.a or event.d or event.space):
            self.walkcount = 0
            if event.last_dir == "a":
                return get_texture(self.stillname)
            if event.last_dir == "d":
                return pygame.transform.flip(get_texture(self.stillname), True, False)
        # if jumping and which direction
        elif event.space:
            self.walkcount = 0
            if event.a and not event.d:
                return get_texture(self.walknames[0])
            else:
                return pygame.transform.flip(get_texture(self.walknames[0]), True, False)
        # if walking and which direction
        elif not event.space:
            self.walkcount += 1
            if event.last_dir == "a":
                return get_texture(self.walknames[self.walkcount // 3])
            if event.last_dir == "d":
                return pygame.transform.flip(get_texture(self.walknames[self.walkcount // 3]), True, False)

    def get_draw_offset(self):
        if event.a:
            self.velocity[0] = self.movingspeed
        if event.d:
            self.velocity[0] = -self.movingspeed
        if not (event.a or event.d):
            self.velocity[0] = 0
        if event.space:
            self.jumping = True
            """
            if self.jumpcount == 1:
                self.velocity[1] = self.jumpspeed
            self.velocity[1] += self.deceleration
            """
        if self.jumping:
            self.jumpcount += 1
            self.velocity[1] = self.jumpspeed - self.jumpcount * self.deceleration
        if self.jumpcount > 20:
            self.jumpcount = 0
            self.velocity[1] = 0
            self.jumping = False
            print("jumpcount reset")
        # gravity
        if not self.jumping:
            self.velocity[1] -= self.gravity_strength
        if self.velocity[1] > 20:
            self.velocity[1] = 20
        # offset
        self.oofset[0] -= self.velocity[0]
        self.oofset[1] -= self.velocity[1]
        return self.oofset

    def blittable_player(self):
        b_player = self.get_player_frame(), self.screen_location
        return b_player


player = Player()
while True:
    event.get_event()
    create_lists()

    screen.fill(pygame.Color("Black"))
    screen.blits(blittablelist)
    player.get_draw_offset()  # SEDA EI KÄPI
    print(player.jumpcount, player.velocity)
    screen.blit(player.blittable_player()[0], player.blittable_player()[1])
    pygame.display.flip()
    clock.tick(60)
