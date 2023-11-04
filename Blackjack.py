import sys
import pygame
import time
from random import randint
from timeit import repeat
from settings import Settings
from money import Money
from cards import Cards
from deck import Deck
from background import Background
from result import Result


class Blackjack:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))        #utworzenie planszy rozgrywki
        pygame.display.set_caption("Blackjack")
        self.money = Money(self)
        self.cards = Cards(self)
        self.deck = Deck()
        self.bg = Background(self)
        self.result = Result(self)
        self.player = []         #talia gracza
        self.croupier = []       #talia krupiera
        self.player_value = []
        self.croupier_value =  []
        self.decision = 0

    def run_game(self):
        while self.settings.money > 0:  
            self.end = False 
            self.croupier_visible = False      
            self.deck.built_deck()
            self.player.clear()                                    #czyszczenie stołu
            self.croupier.clear()
            self.clear()                      
            for i in range(0,2):                                   #dodanie po 2 karty - początek partii
                self.give_card(self.croupier)
                self.give_card(self.player)
            self.count_value_croupier()
            self.count_value_player()
            self._update_screen()
            if  sum(self.croupier_value) == 21:                         #sprawdzenie czy krupier ma blackjack'a - jeśli tak - zakończenie partii
                if sum(self.player_value) == 21:
                    self.croupier_visible = True
                    self.endgame_draw()
                else:
                    self.settings.money -= self.settings.bet
                    self.croupier_visible = True
                    self.endgame_lose()
            else:
                while self.end == False:
                    if sum(self.player_value) == 21:                  #sprawdzenie czy gracz ma blackjack'a - jeśli tak - koniec partii  
                        self.settings.money += 2 * self.settings.bet
                        self.endgame_win()
                        break
                    else:
                        while self.end == False:
                            self._check_events()
                            if self.decision == 1:                        #podjęcie decyzji o dobraniu karty
                                self.give_card(self.player)
                                self._update_screen()
                                self.player_value.clear()
                                self.count_value_player()
                                if sum(self.player_value) > 21:
                                    self.settings.money -= self.settings.bet
                                    self.endgame_lose()
                                    break
                                elif sum(self.player_value) == 21:                  #sprawdzenie czy gracz ma blackjack'a - jeśli tak - koniec partii  
                                    self.settings.money += 2 * self.settings.bet
                                    self.endgame_win()
                                    break
                            elif self.decision == 2:                       #podjęcie decyzji o niedobieraniu więcej kart
                                self.croupier_visible = True
                                self._update_screen()
                                time.sleep(0.5)
                                while self.end == False:
                                    self.clear()
                                    self.count_value_player()
                                    self.count_value_croupier()
                                    if sum(self.croupier_value) > 21:
                                        self.settings.money += self.settings.bet
                                        self.endgame_win()
                                        break
                                    elif sum(self.croupier_value) == 21:
                                        self.settings.money -= self.settings.bet
                                        self.endgame_lose()
                                        break
                                    elif sum(self.croupier_value) < 17: #sprawdzenie suma wartości kart krupiera wynosi mniej niż 17 - jeśli tak - dodanie mu karty
                                        self.give_card(self.croupier)
                                        repeat
                                    elif sum(self.croupier_value) < 21 and sum(self.croupier_value) >= 17: #sprawdzenie czy krupier nie przegrał lub nie potrzebuje karty
                                        if sum(self.croupier_value) == sum(self.player_value):             #zakończenie rozgrywki remisem
                                            self.endgame_draw()
                                            break
                                        elif sum(self.croupier_value) > sum(self.player_value):           #przegrana gracza
                                            self.settings.money -= self.settings.bet
                                            self.endgame_lose()
                                            break
                                        else:                                                             #wygrana gracza
                                            self.settings.money += self.settings.bet
                                            self.endgame_win()
                                            break
                                    

    def _check_events(self):                                                          #sprawdzenie czy jakieś klawisze zostały naciśnięte
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #wyjście z gry
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:    
                self._check_keyup_events(event)
            

    def _check_keydown_events(self, event):                             #naciśnięcie klawisza
        if event.key == pygame.K_LALT:
            self.decision = 1
            time.sleep(0.2)
        elif event.key == pygame.K_LCTRL:
            self.decision = 2 
            time.sleep(0.2) 
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):                               #odciśnięcie klawisza
        if event.key == pygame.K_LALT:
            self.decision = 0
        elif event.key == pygame.K_LCTRL:
            self.decision = 0

    def count_value_player(self):                                       #liczenie wartości kart gracza                       
        for i in range(0,len(self.player)):
            card = self.player[i]
            card_value_list = self.deck.values.get(card)
            card_value = int(card_value_list[0])
            self.player_value.append(card_value)
    
    def count_value_croupier(self):                                     #liczenie wartości kart krupiera                         
        for i in range(0,len(self.croupier)):
            card = self.croupier[i]
            card_value_list = self.deck.values.get(card)
            card_value = int(card_value_list[0])
            self.croupier_value.append(card_value)

    def give_card(self, who):                                           #dobranie karty
        card_deck = self.deck.card_deck                                   
        card = card_deck.pop(randint(0,len(card_deck) - 1))   
        who.append(card)
        self._update_screen()
        time.sleep(0.5)

    def clear(self):
        self.croupier_value.clear()
        self.player_value.clear()

    def endgame_win(self):                                               #zakończenie partii wygraną
        self._update_screen()
        self.result.show_win()
        pygame.display.flip()
        time.sleep(3)
        self.end = True

    def endgame_lose(self):                                             #zakończenie partii porażką
        self._update_screen()
        self.result.show_lose()
        pygame.display.flip()
        time.sleep(3)
        self.end = True

    def endgame_draw(self):                                             #zakończenie partii remisem
        self._update_screen()
        self.result.show_draw()
        pygame.display.flip()
        time.sleep(3)
        self.end = True

    def _update_screen(self):                                          #odświerzanie ekranu
        self.bg.blit_bg()
        self.cards.blitme_player(self.player)
        if self.croupier_visible == True:
            self.cards.blitme_croupier_visible(self.croupier)
        else:
            self.cards.blitme_croupier_not_visible(self.croupier)
        self.money.show_money()
        pygame.display.flip()

if __name__ == '__main__':
    ai = Blackjack()
    ai.run_game()