import sys
import pygame


def check_keydown_events(event, ship):
    #Check key down events
    if event.key == pygame.K_d:
        ship.moving_right = True

    elif event.key == pygame.K_a:
        ship.moving_left = True

    elif event.key == pygame.K_w:
        ship.moving_up = True

    elif event.key == pygame.K_s:
        ship.moving_down = True

def check_keyup_events(event, ship):
    #Check key up events
    if event.key == pygame.K_d:
        ship.moving_right = False

    elif event.key == pygame.K_a:
        ship.moving_left = False

    elif event.key == pygame.K_w:
        ship.moving_up = False

    elif event.key == pygame.K_s:
        ship.moving_down = False

def check_events(ship):
    #Respond to keybpresses and mouse events
    for event in pygame.event.get():
            #Quits the game
            if event.type == pygame.QUIT:
                sys.exit()

            #Check key down events
            if event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship)

            #Check key up events
            if event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

def update_screen(bg_color, screen, ship):
    #Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        ship.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()