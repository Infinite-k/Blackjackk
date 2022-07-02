import random
from blackjackart import logo

def total_calc(card_deck):
    total = 0
    for i in card_deck:
        total += i
    return total

def blackjack_checker(player_cards,computer_cards):
    if total_calc(player_cards) == 21 or total_calc(computer_cards) == 21:
        if total_calc(player_cards) == 21 and total_calc(computer_cards) == 21:
            return False
        elif total_calc(player_cards) == 21:
            return True
        elif total_calc(computer_cards) == 21:
            return False    

def ace(cards):
    for i in cards:
        if i == 11:
            return True



def blackjack():
    victory = ""
    print (logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_cards = [random.choice(cards),random.choice(cards)]
    computer_cards = [random.choice(cards),random.choice(cards)]
    
    print (f"Your cards: {player_cards}, current score: {total_calc(player_cards)} \nComputers first card: {computer_cards[0]}\n")

    if blackjack_checker(player_cards,computer_cards) == True:
        victory = "player"
    elif blackjack_checker(player_cards, computer_cards) == False:
        victory = "comp"   

    while victory == "":
        wants_card = input (f"Type 'y' to get another card, type 'n' to pass:\n")
        
        #FOR PLAYER DAMMIT
        if wants_card == 'y':    
            player_cards.append(random.choice(cards))
            if total_calc(player_cards) > 21:
                for i in range(len(player_cards) -1):
                    if player_cards[i] == 11:
                        player_cards[i] = 1 

            if total_calc(player_cards) > 21:
                victory = "comp"

            elif total_calc(computer_cards) == total_calc(player_cards):
                victory = "draw"
            
            else:
                if blackjack_checker(player_cards,computer_cards) == True:
                    victory = "player"
                elif blackjack_checker(player_cards, computer_cards) == False:
                    victory = "comp"
                else:
                    print (f"\nYour cards: {player_cards} || Current score:{total_calc(player_cards)}\nComputers first card: {computer_cards[0]}\n")
                    
        #FOR COMP DAMMIT
        elif wants_card == "n":
            if not (total_calc(computer_cards)) > 16:
                computer_cards.append(random.choice(cards))
            elif total_calc(computer_cards) > 16:
                if total_calc(player_cards) > total_calc(computer_cards) and not(total_calc(player_cards)) > 21:
                    victory = "player"
                if total_calc(computer_cards) > total_calc(computer_cards) and not(total_calc(computer_cards)) > 21:
                    victory = "computer"

            if total_calc(computer_cards) > 21:
                for i in range(len(computer_cards) -1):
                    if computer_cards[i] == 11:
                        computer_cards[i] = 1 
            if total_calc(computer_cards) > 21:
                victory = "player"
            elif total_calc(computer_cards) == total_calc(player_cards):
                victory = "draw"
            else:
                if blackjack_checker(player_cards,computer_cards) == True:
                    victory = "player"
                elif blackjack_checker(player_cards, computer_cards) == False:
                    victory = "comp"
                else:
                    print (f"\nYour cards: {player_cards} || Current score:{total_calc(player_cards)}\nComputers first card: {computer_cards[0]}\n")

       
    if victory == "comp":
        if blackjack_checker(player_cards,computer_cards) == False:
            print (f"\nYour final hand: {player_cards}, final score: {total_calc(player_cards)}\nComputers final hand: {computer_cards}, Final score: {total_calc(computer_cards)}\nCOMPUTER GETS A BLACKJACK, WHAT WERE THE CHANCES\nAnd you lose :)")
        else:
            print (f"\nYour final hand: {player_cards}, final score: {total_calc(player_cards)}\nComputers final hand: {computer_cards}, Final score: {total_calc(computer_cards)}\nYou lose (loser)\n")
    elif victory == "player":
        if blackjack_checker(player_cards,computer_cards) == True:
            print (f"\nYour final hand: {player_cards}, final score: {total_calc(player_cards)}\nComputers final hand: {computer_cards}, Final score: {total_calc(computer_cards)}\nBLACKJACKKKKK!!\nYOU WIN!!\n")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        else:
            print (f"\nYour final hand: {player_cards}, final score: {total_calc(player_cards)}\nComputers final hand: {computer_cards}, Final score: {total_calc(computer_cards)}\nYou win (Your still a loser tho :)\n")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    else:
        print (f"\nYour final hand: {player_cards}, final score: {total_calc(player_cards)}\nComputers final hand: {computer_cards}, Final score: {total_calc(computer_cards)}\nDRAWWWWWW MATCH.\n")



play = input(f"Do you want to play a game of blackjack, Type 'y', 'n' or '?' to view rules:\n")

if play == "?":
    print ("""
At the beginning of each round, both players are dealt two cards where the dealers(computers) first card is revealed only and both your cards are displayed.

You are given a chance to draw more cards. The players can either ‘hit(draw more cards)’ or ‘stand(skip the turn)’. If the player calls out ‘y’, they are given an extra card. They can then call out ‘n’ if they do not wish to draw any more cards. The player can ‘HIT’ as many times as they wish, but have to aim not to ‘bust’ (exceed a total of 21).

If the player busts, they immediately lose the game.

After you have played and either y or n, the dealer takes their turn. They can, again, either ‘HIT’ or ‘STAND’. If the dealer’s hand exceeds 21, you win immediately.

If the dealer reaches a valid hand, the cards are totalled and each player’s hand is compared to the dealer’s. If the player scored higher than the dealer, they win. If the player ties with the dealer, the game draws. Otherwise, the player loses.

A perfect hand combines an ace with a 10, Jack, Queen or King and is known as a ‘Blackjack’ which is euqual to 21.

Whichever side acquires a blackjack they immeadietly win.""")

    play = input ("Type 'y' or 'n' to play now.")

while play == "y":
    blackjack()
    play = input(f"Do you want to play a game of blackjack, Type 'y' or 'n':\n")















































































############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
