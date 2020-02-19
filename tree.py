import pygame
from pygame.sprite import Sprite
import random

class Ship():

    def __init__(self, screen):
        #Initialize the tree and sets it's starting location
        #bottom rect will always be one pixel above the top of the screen
        #centerx is a random value between screen_rect.left and screen_rect.right

        self.screen = screen

        #Load the ship image and get its rect.
        self.image = pygame.image.load('C:\\Users\\jheal\\Documents\\Programming\\pygame_training\\tree.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.centerx = random(self.screen_rect.left, self.screen_rect.right)
        self.rect.bottom = self.screen_rect.top
        self.pos_x = self.rect.centerx
        self.pos_y = self.rect.centery

        #The speed at which the tree will travel down the screen
        self.speed = 0.5


    def update(self):
        #since you can have a fraction of a pixel we have a second variable, pos_y
        #we make changes to pos_y in incriments and then update self.rect.centery based on pos_y
        #self.rect.centery will be rounded to the nearest whole number.
        self.pos_y += self.speed
        self.rect.centery = self.pos_y

    def blitme(self):
        #Check movement flags and then draw the ship at its current location.
        self.screen.blit(self.image, self.rect)