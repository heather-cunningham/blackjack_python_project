# Ch 22 - Collections of Objs   4/17/17
# Cards Class

##Suits are Spades, Hearts, Diamonds, and Clubs (in descending order in bridge):
##Spades --> 3
##Hearts --> 2
##Diamonds --> 1
##Clubs --> 0

##Ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King.
##Jack --> 11
##Queen --> 12
##King --> 13

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    #NOTE: rank narf is just a placeholder for the 0th element, which won't be used
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10",
             "Jack", "Queen", "King"]
    
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    #----------------------Card Methods------------------------------------------
    #to_string
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

##    comparison method takes two parameters, self and other,
##    and returns 1 if the 1st object is greater,
##    -1 if the second object is greater,
##    and 0 if they are equal to each other.
##    Card suit is higher in importance than card rank
    def compare(self, other):
        """ Returns 1 if the 1st object is greater, -1 if the second object
        is greater, and 0 if they are equal. Suit is higher in importance than
        card rank. Aces are low. """
        # Check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # if suits are the same, check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # If ranks are the same, it’s a tie
        return 0

    def equalTo(self, other):
        return self.compare(other) == 0

    def lessThanOrEqualTo(self, other):
        return self.compare(other) <= 0

    def greaterThanOrEqualTo(self, other):
        return self.compare(other) >= 0

    def greaterThan(self, other):
        return self.compare(other) > 0

    def lessThan(self, other):
        return self.compare(other) < 0

    def notEqual(self, other):
        return self.compare(other) != 0

##    def __equalTo__(self, other):
##        return self.compare(other) == 0
##
##    def __lessThanOrEqualTo__(self, other):
##        return self.compare(other) <= 0
##
##    def __greaterThanOrEqualTo__(self, other):
##        return self.compare(other) >= 0
##
##    def __greaterThan__(self, other):
##        return self.compare(other) > 0
##
##    def __lessThan__(self, other):
##        return self.compare(other) < 0
##
##    def __notEqual__(self, other):
##        return self.compare(other) != 0
#End Class Card-------------------------------

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
                
    #----------------------Deck Methods------------------------------------------
    def print_deck(self):
        for card in self.cards:
            print(card)

    #to_string w/ formatting
##    def __str__(self):
##        deck_str = ""
##        for i in range(len(self.cards)):
##                deck_str = deck_str + " " * i + str(self.cards[i]) + "\n"
##        return deck_str

    # Built in shuffle method
    def shuffle(self):
        import random
        rng = random.Random() # Create a random generator
        rng.shuffle(self.cards) # Use its shuffle method

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    #to Deal a card
    def pop(self):
        return self.cards.pop()

    #Ck if all cards dealt, deck is empty
    def is_empty(self):
        return self.cards == []
    
##        To write your own shuffle method
##    def shuffle(self):
##        import random
##        rng = random.Random() # Create a random generator
##        for i in range( len(self.cards) ):
##            j = rng.randrange(i, len(self.cards) )
##            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])


