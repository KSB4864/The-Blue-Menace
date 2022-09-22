# TITLE SCREEN
#Kashyap Bendapudi
import pygame,sys
import pygame
import random
import sys
import math

pygame.init()
pygame.mixer.music.load('Title_Screen_Music.wav')
pygame.mixer.music.play(-1,0.0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("PRESS SPACE!!!")
clock = pygame.time.Clock()

background_position = [0,0]
#Loads the Title screen astethic
background_image = pygame.image.load("osm titscreen.PNG").convert()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
#Makes it so that you can select between gamemodes with the numpad
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                import osmptt

   

    screen.blit(background_image,background_position)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
