import pygame
from config import *
import math
import random

class spritesheet:
    def __init__(self,file):
        self.sheet=pygame.image.load(file).convert()
    
    def get_sprite(self,x,y,width,height):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        self.layer=PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change=0
        self.y_change=0
        
        self.facing = 'down'

        self.image = self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)


        
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change=0
        self.y_change=0
    
    def movement(self):
        keys =  pygame.key.get_pressed()
        global PLAYER_SPEED
        #if keys[pygame.K_LEFT]:
        #    self.x_change-=PLAYER_SPEED
        #    self.facing = 'left'
        #if keys[pygame.K_RIGHT]:
        #    self.x_change+=PLAYER_SPEED
        #    self.facing = 'right'
        #keys =  pygame.key.get_pressed()
        #if keys[pygame.K_UP]:
        #    self.y_change-=PLAYER_SPEED
        #    self.facing = 'up'
        #if keys[pygame.K_DOWN]:
        #    self.y_change+=PLAYER_SPEED
        #    self.facing = 'down'
            
        if keys[pygame.K_a]:
            if keys[pygame.K_LSHIFT]:
                PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
                self.x_change-=PLAYER_SPEED
                self.facing = 'left' 
                PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION               
            self.x_change-=PLAYER_SPEED
            self.facing = 'left'
            
        if keys[pygame.K_d]:
            if keys[pygame.K_LSHIFT]:
                PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
                self.x_change+=PLAYER_SPEED
                self.facing = 'right'
                PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION   
            self.x_change+=PLAYER_SPEED
            self.facing = 'right'
            
        if keys[pygame.K_w]:
            if keys[pygame.K_LSHIFT]:
                PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
                self.y_change-=PLAYER_SPEED
                self.facing = 'up'
                PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION
            self.y_change-=PLAYER_SPEED
            self.facing = 'up'
            
        if keys[pygame.K_s]:
            if keys[pygame.K_LSHIFT]:
                PLAYER_SPEED = PLAYER_SPEED * SHIFT_CALCULATION
                self.y_change+=PLAYER_SPEED
                self.facing = 'down'
                PLAYER_SPEED = PLAYER_SPEED / SHIFT_CALCULATION
            self.y_change+=PLAYER_SPEED
            self.facing = 'down'
            
class Block(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._LAYER = BLOCK_LAYER
        self.groups=self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x= x*TILESIZE
        self.y = y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(960,448,self.width,self.height)
        
        self.rect=self.image.get_rect()
        self.rect.x = self.x
        self.rect.y=self.y
        
class Ground(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game=game
        self._layer=GROUND_LAYER
        self.groups=self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE
        
        self.image=self.game.terrain_spritesheet.get_sprite(64,352,self.width,self.height)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        