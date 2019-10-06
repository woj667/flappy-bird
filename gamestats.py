import pygame.font


class GameStats:
    def __init__(self, screen, settings):
        # import outside parameters
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        # font properties
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.score_image = self.font.render("X", True, self.text_color, self.settings)
        self.high_score_image = self.font.render("X", True, self.text_color, self.settings)

        # Display actual score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # Display high score at the top left of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = 20

        # scores
        self.score = 0
        self.high_score = 0

        # flags
        self.game_active = False

    def reset_game(self):
        self.game_active = True
        self.score = 0

    def increment_score(self):
        self.score += 1

    def update(self):
        # update high score
        if self.score > self.high_score:
            self.high_score = self.score

        # create strings for scores
        score_str = str(self.score)
        high_score_str = str(self.high_score)

        # render scores
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings)

    def blitme(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
