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
DIRECTION = 'right'
rx = 0
ry = 0
animationcounter = 0

#Sprites and Visual Elements
dogImg = pygame.image.load('sprite_dog.png')
#dogImg.set_clip(pygame.Rect(0,0,60,60))
#frame1 = dogImg.subsurface(dogImg.get_clip())
dogImg.set_clip(pygame.Rect(160,0,80,80))
frame2 = dogImg.subsurface(dogImg.get_clip())

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_w:
                DIRECTION = 'up'
                ry = ry - 5
            elif event.key == K_s:
                DIRECTION = 'down'
                ry = ry + 5
    displaysurf.fill(WHITE)
    if animationcounter > 30:
        animationrcounter = 0
    animationcounter += 1
    displaysurf.blit(frame2, (rx, ry))
    #pygame.draw.rect(displaysurf, BLACK, (rx,ry,100,50))
    pygame.display.update()
