import pygame

class Ship():

    def __init__(self, screen):
        #Initialize the shipo and set its starting position.

        self.screen = screen

        #Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement flags. When they are True the ship will move one px for screen flip
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        #Check movement flags and then draw the ship at its current location.
        if self.moving_right == True:
            self.rect.centerx += 1

        elif self.moving_left == True:
            self.rect.centerx -= 1

        elif self.moving_up == True:
            self.rect.bottom -= 1

        elif self.moving_down == True:
            self.rect.bottom += 1
            
        self.screen.blit(self.image, self.rect)