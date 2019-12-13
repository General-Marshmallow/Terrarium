import pygame
import sys
pygame.init()
window_size = window_width, window_height = 800, 600
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
mouse_pos = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

    screen.fill(pygame.Color("black"))
    screen.blit(pygame.image.load("textures/biskit.jpg"), mouse_pos)
    pygame.display.flip()
    clock.tick(60)