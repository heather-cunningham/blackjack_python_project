# Heather Cunningham
# Ch 22 - Collections of Objs   4/17 -4/21-17

# Hand of 21 (aka BlackJack game)
#--------------------------------
##You are to write a program that creates, populates and shuffles a deck of
##objects of the class Card and then plays a hand of 21 (player against computer,
##computer stands on a score of 19). Your program should output the cards dealt,
##the scores and winner.

import sys
from Cards import Card
from Cards import Deck 
from blackjack_game import Blackjack_Game


def play_game(input_answer):
    if input_answer == "Y":
        return True
    elif input_answer == "N":
        print("Thank you! Play again soon!")
        return False
    else:
        print("Input Error: Answer must be Y or N for yes or no.")
        return play_game(input("Do you want to play? (Y/N)\n").upper())

#test
##new_deck = Deck()
##new_deck.print_deck()

print("Welcome to our virtual Blackjack table! Online gambling is against the law,")
print("so all bets are off.  But, try to beat the computer!")
print("This is single deck, Aces can be high or low Blackjack. Face cards = 10.")
print("Dealer stays on 19. House beats all ties.\n")

players_name = input("Please enter player's name:\n")
answer = input("Do you want to play? (Y/N)\n").upper()

while play_game(answer):
    game = Blackjack_Game(players_name, "Computer")
    deck = Deck()
    players_hand = game.deal_hand(deck)
    deck = game.print_players_hand(players_hand, deck)
    dealers_hand = game.deal_hand(deck)
    deck = game.print_dealers_hand(dealers_hand, deck)
    action_ans = input(game.player
                   + ", do you want to hit or stay? (Enter H or S)").upper()
    deck = game.action(action_ans, dealers_hand, deck)
    play_again = (input("\nDo you want to play again?(Y/N)\n").upper())
    play_game(play_again)
    if play_again == "N":
        break
##else:  
##    sys.exit(0)
    
    
