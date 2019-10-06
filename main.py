import pygame
from bird import Bird
from background import Background
from settings import Settings
from pygame.sprite import Group
from gamestats import GameStats
import game_functions as gf


# Import game settings
settings = Settings()

# Initialize pygame
pygame.init()

# Create user events
ADD_PIPE = gf.create_user_events(settings)

# Setup a clock
clock = pygame.time.Clock()

# Set display's parameters
pygame.display.set_caption(settings.screen_caption)
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

# Check game stats
stats = GameStats(screen, settings)

# Create instances for bird, background and pipes
bird = Bird(screen, settings, stats)
background = Background(screen, settings)
pipes_bottom = Group()
pipes_top = Group()

# draw the screen for the first time
gf.update_screen(screen, background, bird, pipes_bottom, pipes_top, stats)

# enter game loop
while True:
    # check external and interval
    gf.check_events(settings, screen, bird, ADD_PIPE, pipes_bottom, pipes_top, stats)

    # if game is not active freeze the screen and wait for event
    if stats.game_active:
        gf.update_screen(screen, background, bird, pipes_bottom, pipes_top, stats)

    # set FPS - loop with given frame rate
    settings.dt = clock.tick(settings.frames_per_second)
