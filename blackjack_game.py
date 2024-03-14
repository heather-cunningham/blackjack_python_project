#Blackjack_cards Class

from Cards import Card
from Cards import Deck

class Blackjack_Game:

    def __init__(self, player="", dealer=""):
        self.player = player
        self.dealer = dealer
        self.players_hand_vals = []
        self.dealers_hand_vals = []

    #----------------------Methods------------------------------------------
    def deal_card(self, deck):
        deck.shuffle()
        return deck.pop()

    def deal_hand(self, deck):
        faceDown_card = self.deal_card(deck)
        faceUp_card = self.deal_card(deck)
        return (faceDown_card, faceUp_card)

    def assign_face_val(self, card, player):
        if card.rank in range(2, 11):
            return card.rank
        if card.rank in range(11,14):
            return 10
        if card.rank == 1:
            if player == self.player:
                face_val = int(input("\nYou have an Ace; do you want it to be high or low? Enter 1 or 11:\n"))
                return face_val
            else:
                if sum(self.dealers_hand_vals) <= 10:
                    return 11
                else:
                    return 1

    def print_players_hand(self, players_hand, deck):
        (faceDown_card, faceUp_card) = players_hand
        deck.remove(faceDown_card)
        deck.remove(faceUp_card)
        print("\n" + self.player + ", your face-down card is: "
              + str(faceDown_card))
        print(self.player + ", your face-up card is: "
              + str(faceUp_card))
        self.players_hand_vals.append(self.assign_face_val(faceDown_card, self.player))
        self.players_hand_vals.append(self.assign_face_val(faceUp_card, self.player))
        print("\nYour cards are worth = " + str(self.players_hand_vals[0])
              + " + " + str(self.players_hand_vals[1])
              + ". Total = " + str(sum(self.players_hand_vals)) )
        print()        
        return deck
        
    def print_dealers_hand(self, dealers_hand, deck):
        (faceDown_card, faceUp_card) = dealers_hand
        deck.remove(faceDown_card)
        deck.remove(faceUp_card)
        print(self.dealer + "'s face-up card is: "
              + str(faceUp_card))
        self.dealers_hand_vals.append(self.assign_face_val(faceDown_card, self.dealer))
        self.dealers_hand_vals.append(self.assign_face_val(faceUp_card, self.dealer))
        print()
        return deck

    def action(self, input_ans, dealers_hand, deck):
        if input_ans == "H":
            deck = self.hit(self.player, dealers_hand, deck)
            return deck
        elif input_ans == "S":
            deck = self.stay(dealers_hand, deck)
            return deck
        else:
            print("\nInput Error: Answer must be H or S for Hit or Stay.")
            return self.action(input("\nDo you want to hit or stay? (Enter H or S)").upper(), dealers_hand, deck)

    def stay(self, dealers_hand, deck):
        print(self.player + " stays. Player's total is: "
              + str(sum(self.players_hand_vals)) )
        (faceDown_card, faceUp_card) = dealers_hand
        print("\n" + self.dealer + "'s face-down card is: "
              + str(faceDown_card))
        print(self.dealer + " has: " + str(sum(self.dealers_hand_vals)) )
        if sum(self.dealers_hand_vals) < 19:
            print(self.dealer + " has less than 19. " + self.dealer +  " must hit.")
            deck = self.hit(self.dealer, dealers_hand, deck)
        else:
            self.check_4_winner(self.players_hand_vals, self.dealers_hand_vals)
        return deck
                    
    def hit(self, player, dealers_hand, deck):
        new_card = self.deal_card(deck)
        deck.remove(new_card)
        print("\n" + player + " hits - New card is: " + str(new_card) )
        if player == self.player:
            self.players_hand_vals.append(self.assign_face_val(new_card, self.player))
            list_card_vals = self.players_hand_vals 
        if player == self.dealer:
            self.dealers_hand_vals.append(self.assign_face_val(new_card, self.dealer))
            list_card_vals = self.dealers_hand_vals 
        print("\n" + player + "'s cards now are worth = ")
        for face_val in list_card_vals:
            print( str(face_val) + " + ", end="")
        print("\n"+ player + "'s total = " + str(sum(list_card_vals)))
        self.check_4_bust(player, list_card_vals, dealers_hand, deck)
        return deck

    def check_4_bust(self, player, list_of_values, dealers_hand, deck):
        if player == self.player:
            if sum(list_of_values) > 21:
                print("\nSorry, you bust. House wins.")
            else:
                action_ans = input("\nDo you want to hit or stay? (Enter H or S)").upper()
                deck = self.action(action_ans, dealers_hand, deck)
        if player == self.dealer:
            if sum(list_of_values) > 21:
                print("\nHouse busts. You win.")
            elif sum(list_of_values) < 19:
                print(self.dealer + " has less than 19. " + self.dealer +  " must hit.")
                deck = self.hit(self.dealer, dealers_hand, deck)
            elif sum(list_of_values) >= 19 and sum(list_of_values) <= 21:
                print(self.dealer + " stays. " + self.dealer + " has: "+ str(sum(list_of_values)) )
                self.check_4_winner(self.players_hand_vals, self.dealers_hand_vals)
        return deck

    def check_4_winner(self, players_hand_vals, dealers_hand_vals):
        if sum(self.players_hand_vals) > sum(self.dealers_hand_vals):
            print("\n" + self.player + " has: " + str(sum(self.players_hand_vals)) )
            print(self.dealer + " has: " + str(sum(self.dealers_hand_vals)) )
            print(self.player + " wins!")
        elif sum(self.players_hand_vals) < sum(self.dealers_hand_vals):
            print("\n" + self.player + " has: " + str(sum(self.players_hand_vals)) )
            print(self.dealer + " has: " + str(sum(self.dealers_hand_vals)) )
            print(self.dealer + " wins!")
        else:
            print("\n" + self.player + " has: " + str(sum(self.players_hand_vals)) )
            print(self.dealer + " has: " + str(sum(self.dealers_hand_vals)) )
            print("House breaks all ties. House wins!")

    

    #End Class Blackjack_Game


