#utworzenie tali kart i przypisanie im odpowiednich wartości

class Deck:
    def __init__(self):
        self.figures = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.colours = ['Pik', 'Trefl', 'Kier', 'Karo']
        self.card_deck = []
        self.values = {}
    def built_deck(self):
        self.card_deck.clear()
        self.values.clear()
        i = 0
        while i < len(self.figures):
            p = 0
            while p < len(self.colours):
                self.card_deck.append(self.figures[i] + '_' + self.colours[p])
                p += 1
            i += 1

        i = 0
        q = 0
        value = 2
        index = 0

        while index < len(self.card_deck):
            q += 4
            if index < 36:
                while index < q:
                    card = str(self.card_deck[index])
                    self.values[card] = [value]
                    index += 1
                value += 1
            elif index >= 36 and index < len(self.card_deck) - 4:
                value = 10
                while index < len(self.card_deck) - 4:
                    card = str(self.card_deck[index])
                    self.values[card] = [value]
                    index += 1
            else:
                value = 11
                while index >= len(self.card_deck) - 4 and index < len(self.card_deck):
                    card = str(self.card_deck[index])
                    self.values[card] = [value]
                    index += 1 