#wyświetlanie tła

import pygame

class Background:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Images/table.bmp')
        self.bg_rect = self.image.get_rect()
        self.bg_rect.center = self.screen_rect.center

    def blit_bg(self):
        self.screen.blit(self.image, self.bg_rect)