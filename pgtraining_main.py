import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Again!?!?")
    bg_color = (ai_settings.bg_color)

    ship = Ship(screen)

    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(bg_color, screen, ship)
        

run_game()
