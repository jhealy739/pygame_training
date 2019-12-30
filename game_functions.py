import sys
import pygame

def check_events(ship):
    #Respond to keybpresses and mouse events
    for event in pygame.event.get():
            #Quits the game
            if event.type == pygame.QUIT:
                sys.exit()

            #Check key down events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True

                elif event.key == pygame.K_UP:
                    ship.moving_up = True

                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True

            #Check key up events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

                elif event.key == pygame.K_UP:
                    ship.moving_up = False

                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False

def update_screen(bg_color, screen, ship):
    #Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        ship.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()