import pygame

from pygame.sprite import Group

from settings import Settings

from butt import Ship

import game_functions as gf


def run_game():
    """initialize game and create a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Poop Master")

    # make a butt
    ship = Ship(ai_settings, screen)
    # make a group to store poops in
    bullets = Group()

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
