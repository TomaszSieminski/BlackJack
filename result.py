#wyświetlanie komunikatu jak zakończyła się partia

import pygame.font

class Result:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings 
        self.text_color = (226, 230, 225)
        self.font = pygame.font.SysFont(None,65)
        self.prep_win()
        self.prep_lose()
        self.prep_draw()
    
    def prep_win(self):                                                                         #... w przypadku wygranej
        self.win_image = self.font.render("Win", True, self.text_color, self.settings.bg_color)
        self.win_rect = self.win_image.get_rect()
        self.win_rect.left = self.screen_rect.left + 600
        self.win_rect.top = 300
    def prep_lose(self):                                                                        #... w przypadku porażki
        self.lose_image = self.font.render("Lost", True, self.text_color, self.settings.bg_color)
        self.lose_rect = self.lose_image.get_rect()
        self.lose_rect.left = self.screen_rect.left + 600
        self.lose_rect.top = 300
    def prep_draw(self):                                                                        #... w przypadku remisu
        self.draw_image = self.font.render("Draw", True, self.text_color, self.settings.bg_color)
        self.draw_rect = self.draw_image.get_rect()
        self.draw_rect.left = self.screen_rect.left + 600
        self.draw_rect.top = 300

    def show_win(self):
        self.screen.blit(self.win_image, self.win_rect)
    def show_lose(self):
        self.screen.blit(self.lose_image, self.lose_rect)
    def show_draw(self):
        self.screen.blit(self.draw_image, self.draw_rect)