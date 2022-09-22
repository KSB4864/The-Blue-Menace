
#Period 6
#Part 1: the chalice
#note: most instructions will be the same per level
import pygame
from pygame.locals import*
pygame.init()
pygame.mixer.music.load('ttm.wav')
pygame.mixer.music.play(-1,0.0)

import arcade
BLACK = (0,0,0)
WHITE = (129, 131, 145)
RED = (255,0,0)
BLUE = (136, 96, 204)
GREEN = (0,255,0)
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

#Player's Movements
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
        #self.jump_sound = arcade.load_sound('Jump.wav')
        
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
#gravity
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            
        if self.rect.y >= 485 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 485
            self.frame_since_collision = 0
            self.jump_ok = True

    def jump(self,block):
        if self.jump_ok:
            #arcade.play_sound(self.jump_sound)
            jump.play()
            self.change_y = -8


    #level creation
def create_level1(block_list,all_sprites_list,player):
    block = Platform(WHITE,100,20)
    block.rect.x = 50
    block.rect.y = 350
    block.change_y = 1
    block.boundary_bottom = 485
    block.boundary_top = 300
    block.player = player
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(BLUE,100,20)
    block.rect.x = 250
    block.rect.y = 300
    block.change_x = 5
    block.boundary_left = 225
    block.boundary_right = 400
    block.player = player
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(WHITE,100,20)
    block.rect.x = 550
    block.rect.y = 150
    block.change_y = -1
    block.boundary_bottom = 300
    block.boundary_top = 100
    block.player = player
    block_list.add(block)
    all_sprites_list.add(block)
    
    walls = [ [690,0,20,250,WHITE],
        [690,350,20,250,WHITE],
        [870,0,80,290,WHITE],
        [780,350,20,250,WHITE],
        [799,0,760,70,WHITE],
         ]
        
        
    for item in walls:
        wall = Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)
        all_sprites_list.add(wall)


# init 
pygame.init()
size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("You are the MENACE")
background_position = [0,0]
background_image = pygame.image.load("DeathInbound.png").convert()
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
player = Player(20,15)
player.rect.x = 340
player.rect.y = 485
jump = pygame.mixer.Sound('Jump.wav')
all_sprites_list.add(player)
create_level1(block_list,all_sprites_list,player)


    



done = False
clock = pygame.time.Clock()
#main loop
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
    #can import
    if player.rect.x>=700:
        import osmpt0
   
    screen.blit(background_image,background_position)
    all_sprites_list.update()
    
    
    all_sprites_list.draw(screen)
    #update
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


