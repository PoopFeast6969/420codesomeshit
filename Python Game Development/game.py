import pygame, sys
from pygame.locals import *

pygame.init()

#Game Window
displaysurf = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Raisin Simulator')

#Color Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Gameplay Variables
DIRECTION = 'none'

rx = 0
ry = 0

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_w:
                DIRECTION = 'up'
            elif event.key == K_s:
                DIRECTION = 'down'
        if DIRECTION == 'up':
            ry -= 5
        if DIRECTION == 'down':
            ry += 5
    displaysurf.fill(WHITE)
    pygame.draw.rect(displaysurf, BLACK, (rx,ry,100,50))
    pygame.display.update()
