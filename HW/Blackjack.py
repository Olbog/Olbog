'''4. Написать игру Блэк-джек (https://ru.wikipedia.org/wiki/Блэкджек#Правила)
На старте игры формируется колода из 52 карт 2-10, J, D, K, T (♠️ ♣️ ♥️ ♦️)
Игроку и компьютеру выдается 2 случайные карты
Считается количество набранных очков T = 11 или 1 очко (11 пока общая сумма меньше 21, далее 1), J, D, K = 10, остаьлные по номиналу
Побеждает тот, у кого набралось количество очков равное 21
если победителя нет, игрок может либо потянуть новую карту из колоды (hit) либо нет (pass)
когда игрок сделал все свои ходы вскрываются карты компьютера
Поюеждает тот у кого набрано больше очков
Либо ничья в случае с 21
Если о обоих нет выигрышной комбинации то по очереди добавляется по одной карте и колоды, вначале игроку, потом компьютеру
Если набрано более 21 очков, это проигрыш

Можно добавить:
4.1 Несколько колод для перетосовки
4.2 Денежные ставки
4.3 Таблицу рузельтатов '''


from itertools import product # возвращает «декартово произведение»
from random import shuffle

player_name = input('Please enter your name: ') # ввод имени игрока
count_of_decks = int(input('Enter the number of desks: ')) # ввод кол-во колод карт для данной сессии

suits_card = ['♥️', '♦️', '♣️', '♠️']
number_card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']



class Deck:

    def __init__(self):
        self.cards = self._new_deck()
        shuffle(self.cards)

    def _new_deck(self):
        cards = []
        for suit, number in product(suits_card, number_card):
            if number == 'ace':
                points = 11
            elif number.isdigit():
                points = int(number)
            else:
                points = 10
            card_1 = Card(suit=suit, number=number, points=points)
            cards.append(card_1)
        return cards
    
    # Выдает карту из колоды и удаляет ее оттуда
    
    def card_get(self): 
        return self.cards.pop()


class Card:

    def __init__(self, suit, number, points):
        self.suit = suit
        self.rank = number
        self.points = points


class Game:
    pass


class Player:
    pass

class Results:
    pass


        
        



