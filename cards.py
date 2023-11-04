#wyświetlanie kart

import pygame

class Cards:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Images/back.bmp')
        self.card_rect = self.image.get_rect()

    def blitme_player(self, who):                                           #wyświetlanie kart gracza
        self.card_rect.left = 570
        self.card_rect.top =  400
        for i in range(len(who)):
            self.image = pygame.image.load('Images/{}.bmp'.format(who[i]))
            self.screen.blit(self.image,self.card_rect)
            self.card_rect.left += 50

    def blitme_croupier_visible(self, who):                                 #wyświetlanie wszystkich kart krupiera
        self.card_rect.left = 570
        self.card_rect.top =  100
        for i in range(len(who)):
            self.image = pygame.image.load('Images/{}.bmp'.format(who[i]))
            self.screen.blit(self.image,self.card_rect)
            self.card_rect.left += 50

    def blitme_croupier_not_visible(self, who):                            #wyświetlanie jednej odkrytej i jednej zakrytej karty krupiera
        self.card_rect.left = 570
        self.card_rect.top =  100
        for i in range(len(who)):
            if i == 0:
                self.image = pygame.image.load('Images/{}.bmp'.format(who[0]))
                self.screen.blit(self.image,self.card_rect)
                self.card_rect.left += 50
            else:
                self.image = pygame.image.load('Images/back.bmp')
                self.screen.blit(self.image,self.card_rect)