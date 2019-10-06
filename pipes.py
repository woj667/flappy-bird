import pygame
from pygame.sprite import Sprite


class Pipe(Sprite):
    def __init__(self, screen, settings, pipe_top_height, image, stats):
        # supercharge Pipe
        super().__init__()
        # take outside parameters
        self.screen = screen
        self.settings = settings
        self.pipe_top_height = pipe_top_height
        self.image = pygame.image.load(image)
        self.stats = stats

        # get pipe's and screen's dimensions
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # align position at the screen - this is abstract class <- this operation will never happen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def update(self):
        # move pipe to the left
        self.rect.centerx -= self.settings.pipe_speed

        # kill pipe if leaves the screen
        if self.rect.right <= 0:
            pygame.sprite.Sprite.kill(self)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class PipeBottom(Pipe):
    def __init__(self, screen, settings, pipe_top_height, stats):
        # take image's path
        image = "images/bottom.png"
        super().__init__(screen, settings, pipe_top_height, image, stats)

        # Start each new pipe at the point:
        self.rect.left = self.settings.screen_width
        self.rect.top = self.pipe_top_height + self.settings.pipe_gap

    def reset_pipe(self):
        self.rect.left = self.settings.screen_width
        self.rect.top = self.pipe_top_height + self.settings.pipe_gap


class PipeTop(Pipe):
    def __init__(self, screen, settings, pipe_top_height, stats):
        # take image's path
        image = "images/top.png"
        super().__init__(screen, settings, pipe_top_height, image, stats)

        # Start each new pipe at the point:
        self.rect.left = self.settings.screen_width
        self.rect.bottom = self.pipe_top_height

    def reset_pipe(self):
        self.rect.left = self.settings.screen_width
        self.rect.bottom = self.pipe_top_height

    def update(self):
        # use update() from Pipe class...
        super().update()

        # ...but also increment score after the pipe leaves the screen
        if self.rect.right <= 0:
            self.stats.increment_score()
