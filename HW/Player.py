import random



class Player():

    def __init__(self):
        self.cards = []
        self.full_points = 0

    def points(self):
        self.full_points = sum(card.points for card in self.cards)

    def take_card(self, card):
        self.cards.append(card)
        self.points()


    def print_cards(self):
        print(self, " data")
        for card in self.cards:
            print(card)
        print('Full points: ', self.full_points)



class Dealer(Player):

    max_points = 17


    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False