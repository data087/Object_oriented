class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit('Diamond', '◆'), Suit('Heart', '♥'), Suit('Spade', '♠')
cards = [AceCard('A', Spade), NumberCard('2', Spade), NumberCard('3', Spade)]


def card(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
    else:
        raise Exception("Rank out of range")


def card2(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    else: # else문은 확신할때만 사용할 것. card 함수가 더 좋음.
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit) # too bad?


def card3(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif rank == 11:
        return FaceCard('J', suit)
    elif rank == 12:
        return FaceCard('Q', suit)
    elif rank == 13:
        return FaceCard('K', suit)
    else:
        raise Exception("Rank out of range")

def card4(rank, suit):
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard, 13:FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)

#deck2 = [card2(rank, suit) for rank in range(13) for suit in (Club, Diamond, Heart, Spade)]
