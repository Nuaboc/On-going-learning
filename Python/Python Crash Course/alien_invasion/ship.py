import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and set its rect
        a = pygame.image.load('images/ship.bmp')
        b = pygame.image.load('images/butt.png')
        while True:
            butt = a + b
        self.image = butt

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for the ship center
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags"""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect  object from self.center
        self.rect.centerx = self.center

    #def animation(self):
        """"""
        butt =
       # while True:
            pygame.image.load('images/ship.bmp')
            pygame.image.load('images/butt.png')
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
