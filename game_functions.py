import pygame
from random import randint
from pipes import PipeBottom, PipeTop
import sys


def check_events(settings, screen, bird, ADD_PIPE, pipes_bottom, pipes_top, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, bird, pipes_bottom, pipes_top, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # left for future use
            # mouse_x, mouse_y = pygame.mouse.get_pos()
            pass
        elif event.type == ADD_PIPE:
            add_pipes(screen, settings, pipes_bottom, pipes_top, stats)


def check_keydown_events(event, bird, pipes_bottom, pipes_top, stats):
    if event.key == pygame.K_SPACE:
        if not stats.game_active:
            reset_game(bird, pipes_bottom, pipes_top, stats)
        bird.initiate_jump()


def check_keyup_events(event):
    if event.key == pygame.K_q:
        sys.exit()


def update_screen(screen, background, bird, pipes_bottom, pipes_top, stats):
    # update background
    background.update()
    background.blitme()

    # update bottom pipe
    for pipe in pipes_bottom:
        pipe.update()
    pipes_bottom.draw(screen)

    # update top pipe
    for pipe in pipes_top:
        pipe.update()
    pipes_top.draw(screen)

    # update bird
    bird.update()
    bird.blitme()

    # update stats
    stats.update()
    stats.blitme()

    # run collision detection
    detect_collision(bird, pipes_bottom, pipes_top)

    # make the most recently drawn screen visible
    pygame.display.flip()


def create_user_events(settings):
    # create a custom event for adding a new pipe
    ADD_PIPE = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_PIPE, settings.pipe_interval)

    return ADD_PIPE


def add_pipes(screen, settings, pipes_bottom, pipes_top, stats):
    # randomize height of the top pipe
    pipe_top_height = randint(200, settings.screen_height - 200)

    # create bottom pipe
    new_bottom_pipe = PipeBottom(screen, settings, pipe_top_height, stats)
    pipes_bottom.add(new_bottom_pipe)

    # create top pipe
    new_top_pipe = PipeTop(screen, settings, pipe_top_height, stats)
    pipes_top.add(new_top_pipe)


def detect_collision(bird, pipes_bottom, pipes_top):
    # check top and bottom collisions
    bird_and_pipe_bottom_collision = pygame.sprite.spritecollide(bird, pipes_bottom, False)
    bird__and_pipe_top_collision = pygame.sprite.spritecollide(bird, pipes_top, False)

    # kill the bird if collides with pipe
    if bird_and_pipe_bottom_collision or bird__and_pipe_top_collision:
        bird.kill_bird()


def reset_game(bird, pipes_bottom, pipes_top, stats):
    # kill bottom pipes
    for pipe in pipes_bottom:
        pygame.sprite.Sprite.kill(pipe)

    # kill top pipes
    for pipe in pipes_top:
        pygame.sprite.Sprite.kill(pipe)

    # reset bird
    bird.reset_bird()

    # reset stats
    stats.reset_game()
