from random import shuffle

class Card:
    suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        cardName = f'{self.values[self.value]} of {self.suits[self.suit]}'
        return cardName

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(2, 15):
                card = Card(i, j)
                self.cards.append(card)
        shuffle(self.cards)
    
    def rem_card(self):
        return self.cards.pop()
    
    def draw(self, p1, c1, p2, c2):
        drawSatement = f'{p1} drew {c1} | {p2} drew {c2}'
        print(drawSatement)

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0
    
class Game:
    def __init__(self):
        name1 = input('Player 1 Name: ')
        name2 = input('Player 2 Name: ')
        print()
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, name):
        print(f'{name} wins this round.')
    
    def draw(self, p1, c1, p2, c2):
        print(f'{p1} drew {c1} | {p2} drew {c2}')

    def gameLoop(self):
        running = True
        cards = self.deck.cards
        while len(cards) >= 2 and running == True:
            # each player draws a card
            card1 = self.deck.rem_card()
            card2 = self.deck.rem_card()
            p1name = self.p1.name
            p2name = self.p2.name
            self.draw(p1name, card1, p2name, card2)

            # if one is higher then
            if card1 > card2:
                self.p1.wins += 1
                self.wins(p1name)
            if card1 < card2:
                self.p2.wins += 1
                self.wins(p2name)

            print(f'The current score is:\n{p1name}: {self.p1.wins} | {p2name}: {self.p2.wins}\n')
            userInput = input('\nPress any key to play another round or type \'q\' to quit')
            if userInput == 'q':
                running = False
                
        # win screen
        wins = self.winner()
        print(f'War is over! {wins}')
        
    def winner(self):
        if self.p1.wins > self.p2.wins:
            return f'{self.p1.name} wins!'
        if self.p1.wins < self.p2.wins:
            return f'{self.p2.name} wins!'
        if self.p1.wins == self.p2.wins:
            return "It was a tie!"
            
game = Game()
game.gameLoop()