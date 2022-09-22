# TITLE SCREEN
#Giulio Poncia
import pygame,sys

import random

import math
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("GAME OVER")
clock = pygame.time.Clock()

score = 0
x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10
background_position = [0,0]
background_image = pygame.image.load("The Menace is dead.png").convert()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                import Title_screen
   

    screen.blit(background_image,background_position)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
            

