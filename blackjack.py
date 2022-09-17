import random 
import os
clear = lambda: os.system('cls')

def deal_card():
    # 1. Returns a random card from the deck.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10]
    card = random.choice(cards)
    return card

def calcluate_score(cards):
    """ Take a list of cards and return the score calucalated from the cards"""
        # 2. Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

        # 3. Inside calculate_score() check for an 11 (ace). If the score is already over 21, remoce the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, bot_score):
    if user_score == bot_score:
        return "Draw :)"
    elif bot_score == 0:
        return "You Lose, the opponent has Blackjack. o_o"
    elif user_score == 0:
        return "You Win with a Blackjack. Sheeeesh!"
    elif user_score > 21:
        return "You went over. You lose ;_;"
    elif bot_score > 21:
        return "Opponent went over. You Win :D" 
    elif user_score > bot_score:
        return "You win :D"
    else:
        return "You lose. T_T" 


def blackjack():
    user_cards = []
    bot_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        bot_cards.append(deal_card())



    # 6. The score will need to be rechecked with every new card drwan and the checks in 4. need to be repeated until the game ends.
    while not game_over:
        # 4. Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calcluate_score(user_cards)
        bot_score = calcluate_score(bot_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {bot_cards[0]}")


        if user_score == 0 or bot_score > 21 or user_score > 21:
            game_over = True
        # 5. If the game has not ened, ask the user if they want to drwaw another card. If yes, the nsue the deal_card() function to add another card to hte user_cards List. If no, then the game has ended.
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y" or choice == "Y":
                user_cards.append(deal_card())
            else:
                game_over = True


    # 7. Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a sore less than 17.
    while bot_score != 0 and bot_score < 17:
        bot_cards.append(deal_card())
        bot_score = calcluate_score(bot_cards)


    # 8. Create a funvtion called compare() and pass in the user_score and bot_score. If the computer and user both have the same score, then it's a draw. 
        # If the computer has a blackjack (0), then the user loses. 
        # If the user has a blackjack (0), then the user wins. 
        # If the user_score is over 21, then the user loses.
        # If the bot_score is over 21, then the computer loses.
        # If none of the above, then the player with the highest score wins.

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {bot_cards}, final score: {bot_score}")
    print(compare(user_score, bot_score))


# 9. Ask the user if the wanna restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y" or "Y":
    clear() 
    blackjack()

