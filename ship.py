import pygame

class Ship():

    def __init__(self, screen):
        #Initialize the shipo and set its starting position.

        self.screen = screen

        #Load the ship image and get its rect.
        self.image = pygame.image.load('D:\\Programming\\Python\\pygame_training\\ship.bmp')
        self.image_right = pygame.image.load('D:\\Programming\\Python\\pygame_training\\ship_right.bmp')
        self.image_left = pygame.image.load('D:\\Programming\\Python\\pygame_training\\ship_left.bmp')
        #self.image = pygame.image.load('C:\\Users\\jheal\\Documents\\Programming\\pygame_training\\ship.bmp')
        #self.image_right = pygame.image.load('C:\\Users\\jheal\\Documents\\Programming\\pygame_training\\ship_right.bmp')
        #self.image_left = pygame.image.load('C:\\Users\\jheal\\Documents\\Programming\\pygame_training\\ship_left.bmp')
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

        #Set the ship speed and velocity
        self.speed = 0.001
        self.xvelocity = 0.0
        self.yvelocity = 0.0


    def update(self):

        #Update the ships rect position based on movement flags
        if (self.moving_right) & (self.xvelocity < 1.5):
            self.xvelocity += self.speed
            #self.pos_x += self.xspeed
            #self.rect.centerx = self.pos_x

        if (self.moving_left) & (self.xvelocity > -1.5):
            self.xvelocity -= self.speed
            #self.pos_x -= self.xspeed
            #self.rect.centerx = self.pos_x

        if (self.moving_up) & (self.yvelocity > -1.5):
            self.yvelocity -= self.speed
            #self.rect.centery = self.pos_y

        if (self.moving_down) & (self.yvelocity < 1.5):
            self.yvelocity += self.speed
            #self.rect.centery = self.pos_y

        if (self.xvelocity >= 0) & (self.rect.right < self.screen_rect.right):
            self.pos_x += abs(self.xvelocity)
            self.rect.centerx = self.pos_x

        if (self.xvelocity <= 0) & (self.rect.left > self.screen_rect.left):
            self.pos_x -= abs(self.xvelocity)
            self.rect.centerx = self.pos_x
            
        if (self.yvelocity <= 0) & (self.rect.top > self.screen_rect.top):
            self.pos_y -= abs(self.yvelocity)
            self.rect.centery = self.pos_y

        if (self.yvelocity >= 0) & (self.rect.bottom < self.screen_rect.bottom):
            self.pos_y += abs(self.yvelocity)
            self.rect.centery = self.pos_y

    def blitme(self):
        #Check movement flags and then draw the ship at its current location.
        if self.moving_right:
            self.screen.blit(self.image_left, self.rect)

        elif self.moving_left:
            self.screen.blit(self.image_left, self.rect)

        else:
            self.screen.blit(self.image, self.rect)