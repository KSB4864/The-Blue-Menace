
#OSM code
import pygame
from pygame.locals import*

import arcade
BLACK = (116, 80, 138)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (129, 131, 145)
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class Platform(pygame.sprite.Sprite):
    player = None
    change_x = 0         
    change_y = 0
    boundary_top = 0
    boundary_bottom = 0
    boundary_right = 0
    boundary_left = 0

    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.change_x
        hit = pygame.sprite.collide_rect(self,self.player)
        if hit:
            if self.change_x > 0:
                player.rect.right = self.rect.left
            else:
                player.rect.left = self.rect.right
                
        self.rect.y += self.change_y
        hit = pygame.sprite.collide_rect(self,self.player)
        if hit:                
            if self.change_y < 0:
                player.rect.bottom = self.rect.top
            else:
                player.rect.top = self.rect.bottom
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
        if self.rect.x < self.boundary_left or self.rect.x > self.boundary_right:
            self.change_x *= -1

#Players Movements
class Player(pygame.sprite.Sprite):
    change_x = 0         
    change_y = 0
    jump_ok = True
    frame_since_collision = 0
    block_list = None
    def __init__(self,x,y):
        super().__init__()   
        self.image = pygame.Surface([15,15])
        self.image = pygame.image.load('The Menace Charsprite.png').convert()
        self.rect = self.image.get_rect()   
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self,block_list,False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
                
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self,block_list,False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.jump_ok = True

            self.frame_since_collision = 0

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

            self.change_y = 0

        if self.frame_since_collision > 6:
            self.jump_ok = False

        self.frame_since_collision += 1

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            
        if self.rect.y >= 685 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 685
            self.frame_since_collision = 0
            self.jump_ok = True

    def jump(self,block):
        if self.jump_ok:
            jump.play()
            self.change_y = -8


    
def create_level1(block_list,all_sprites_list,player):
    block = Platform(GREEN,160,50)
    block.rect.x = 50
    block.rect.y = 350
    block.change_y = 1
    block.boundary_bottom = 485
    block.boundary_top = 300
    block.player = player
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(BLACK,100,10)
    block.rect.x = 250
    block.rect.y = 300
    block.change_x = 3
    block.boundary_left = 215
    block.boundary_right = 400
    block.player = player
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(WHITE,100,20)
    block.rect.x = 550
    block.rect.y = 150
    block.change_y = -4
    block.boundary_bottom = 610
    block.boundary_top = 90
    block.player = player
    block_list.add(block)
    all_sprites_list.add(block)
    
    walls = [ [690,0,20,250,WHITE],
        [690,370,20,330,WHITE],
        [870,0,80,300,WHITE],
        [780,350,20,255,WHITE],
        [799,0,750,70,WHITE],
        [799,0,760,90,WHITE],
        [0,0,20,800,WHITE],
         ]
        
        
    for item in walls:
        wall = Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)
        all_sprites_list.add(wall)


    
pygame.init()
size = [700,700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Watch Out for Pits")
background_position = [0,0]
background_image = pygame.image.load("S2.png").convert()
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
player = Player(20,15)
player.rect.x = 100
player.rect.y = 300
all_sprites_list.add(player)
jump = pygame.mixer.Sound('Jump.wav')
create_level1(block_list,all_sprites_list,player)


    



done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_x = -6
                if event.key == pygame.K_RIGHT:
                    player.change_x = 6
                if event.key == pygame.K_UP:
                    player.jump(block_list)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_x = 0
            if event.key == pygame.K_RIGHT:
                player.change_x = 0
            if event.key == pygame.K_UP:
                player.change_y = 0
    if player.rect.y >= 615:
        import gameover
    if player.rect.x>=700:
        import osmpt1
    if player.rect.x<=-20:
        player.rect.x = 699
    screen.blit(background_image,background_position)
    all_sprites_list.update()
    
    
    all_sprites_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


