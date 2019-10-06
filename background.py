import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load("images/background.png")
        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

    def update(self):
        pass

    def blitme(self):
        self.screen.blit(self.image, self.rect)
