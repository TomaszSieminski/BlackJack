#wyświetlanie ilości pieniędzy

import pygame.font

class Money:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.text_color = (226, 230, 225)
        self.font = pygame.font.SysFont(None,65)

    def show_money(self):
        self.money_str = str(self.settings.money) + " $"
        self.money_image = self.font.render(self.money_str, True, self.text_color, self.settings.bg_color)
        self.money_rect = self.money_image.get_rect()
        self.money_rect.right = self.screen_rect.right - 20
        self.money_rect.top = 20
        self.screen.blit(self.money_image, self.money_rect)
