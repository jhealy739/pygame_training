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
        self.pos_x = self.rect.centerx
        self.pos_y = self.rect.centery

        #Movement flags. When they are True the ship will move one px for screen flip
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Set the ship speed from Settings class
        self.speed = .5

        print (self.pos_x)


    def update(self):
        #Update the ships rect position based on movement flags
        if ((self.moving_right) & (self.rect.right < self.screen_rect.right)):
            self.pos_x += self.speed
            self.rect.centerx = self.pos_x

        if ((self.moving_left) & (self.rect.left > self.screen_rect.left)):
            self.pos_x -= self.speed
            self.rect.centerx = self.pos_x

        if ((self.moving_up) & (self.rect.top > self.screen_rect.top)):
            self.pos_y -= self.speed
            self.rect.centery = self.pos_y

        if ((self.moving_down) & (self.rect.bottom < self.screen_rect.bottom)):
            self.pos_y += self.speed
            self.rect.centery = self.pos_y

    def blitme(self):
        #Check movement flags and then draw the ship at its current location.
        self.screen.blit(self.image, self.rect)