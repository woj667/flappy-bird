import pygame
import math


class Bird:
    def __init__(self, screen, settings, stats):
        # take outside parameters
        self.screen = screen
        self.settings = settings
        self.stats = stats

        # import images from directory
        self.images = dict()
        for key in ('bird0', 'bird1', 'bird2', 'birddead'):
            image_path = "images/" + key + ".png"
            image = pygame.image.load(image_path)
            self.images[key] = image

        # set idle image
        self.image = self.images['bird0']

        # get bird's and screen's dimensions
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # count bird's x and y velocity
        self.flap_vel_x = self.settings.flap_vel * math.cos(math.radians(self.settings.flap_angle))
        self.flap_vel_y = self.settings.flap_vel * math.sin(math.radians(self.settings.flap_angle))

        # Start each new bird at the point:
        self.centerx = self.settings.bird_centerx
        self.centery = self.settings.bird_centery

        # send x,y to object
        self.rect.centerx = int(self.centerx)
        self.rect.centery = int(self.centery)

        # Time from start of the jump
        self.time = 0

        # flags
        self.dead = False

    def kill_bird(self):
        self.dead = True

    def reset_bird(self):
        # Start each new bird at the point:
        self.centerx = self.settings.bird_centerx
        self.centery = self.settings.bird_centery

        # Time from start of the jump
        self.time = 0

        # reset flag
        self.dead = False

    def initiate_jump(self):
        if not self.dead:
            self.time = 0

    def update(self):
        # update delta time between next calls
        self.time += self.settings.dt / 1000

        # calculate vectors
        dy = float(self.flap_vel_y * self.time - 0.5 * self.settings.gravity * self.time ** 2)
        dx = float(self.flap_vel_x * (self.settings.dt / 1000))

        # store float x,y coordinates
        self.centery -= dy
        self.centerx += dx

        # send x,y to object
        self.rect.centerx = int(self.centerx)
        self.rect.centery = int(self.centery)

        # replace states of flight after given time
        if self.time >= self.settings.flap_time:
            self.image = self.images['bird1']
        else:
            self.image = self.images['bird2']

        # check bottom edge and kill the bird if leaves the screen
        if self.rect.bottom >= self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height
            self.dead = True
            self.stats.game_active = False

        # check top edge
        if self.rect.top <= 0:
            self.rect.top = 0
            self.dead = True

        # replace image if bird is dead
        if self.dead:
            self.image = self.images['birddead']

    def blitme(self):
        self.screen.blit(self.image, self.rect)
