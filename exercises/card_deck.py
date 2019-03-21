class Card:
  def __init__(self, suit='H', rank=1):
    self.suit = suit
    self.rank = rank

class Deck:
  suits = 'CDHS'
  ranks = range(1,14)

  def __init__(self):
    self.cards = []

    for suit in self.suits:
      for rank in self.ranks:
        self.cards.append(Card(suit, rank))

  def show_cards(self):
    for card in self.cards:
      print(card.suit + str(card.rank))

deck = Deck()
deck.show_cards()
