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
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

def cards_over_21():
    over_21 = True
    while over_21:
        num1 = random.choice(cards)
        num2 = random.choice(cards)
        if num1 + num2 > 21:
            continue
        else:
            over_21 = False
            return num1, num2

def ace(input_cards):
    if 11 in input_cards:
        original_pos = input_cards.index(11)
        input_cards.remove(11)
        if sum(input_cards) > 10:
            input_cards.insert(original_pos, 1)
        else:
            input_cards.insert(original_pos, 11)
        

want_to_play = input('Do you want to play blackjack? type y or n: ').lower()
player_cards = []
computer_cards = []
playing = False

if want_to_play == 'y':
    playing = True
    went_over = False
    while playing:
        print(logo)
        player_num_1 = random.choice(cards)
        player_num_2 = random.choice(cards)
        if player_num_1 + player_num_2:
            player_num_1, player_num_2 = cards_over_21()
        computer_num_2 = random.choice(cards)
        computer_num_1 = random.choice(cards)
        if computer_num_1 + computer_num_2:
            computer_num_1,computer_num_2 = cards_over_21()
    
        player_cards.append(player_num_1)
        player_cards.append(player_num_2)
        computer_cards.append(computer_num_1)
        computer_cards.append(computer_num_2)
        # print(f"Your cards: [{player_num_1}, {player_num_2}], current_score: {player_num_1 + player_num_2}")
        print(player_cards)
        print(f"Opponent's first card is {computer_num_1}")
        hit = input("Type 'y' to hit type 'n' to stand: ").lower()
        hitting = False
        if hit == 'y':
            hitting = True
            player_cards.append(random.choice(cards))
            ace(player_cards)
            print(f'{player_cards} Total: {sum(player_cards)}')
            if sum(player_cards) > 21:
                print('You went over. You lose ${random.randrange(200,1000)}')
                print(f'Computer cards: {computer_cards}')
                hitting = False
                playing = False
                went_over = True
        else:
            playing = False
        while hitting:
            hit_again = input("Type 'y' to hit type 'n' to stand: ")
            if hit_again == 'y':
                hitting = True
                player_cards.append(random.choice(cards))
                ace(player_cards)
                print(f'{player_cards} Total: {sum(player_cards)}')
                if sum(player_cards) > 21:
                    print(f'You went over. You lose  ${random.randrange(200,1000)}')
                    print(f'Computer cards: {computer_cards}')
                    hitting = False
                    playing = False
                    went_over = True
    
            else:
                hitting = False
                break
                playing = False
        if playing == True:
            computer_hitting = True
            while computer_hitting:
                if sum(computer_cards) <= 15:
                    computer_cards.append(random.choice(cards))
                    ace(computer_cards)
                    if sum(computer_cards) > 21:
                        print(f'Opponent went over. You win ${random.randrange(200,1000)}')
                        print(f'Opponent cards: {computer_cards} Total: {sum(computer_cards)}')
                        playing = False
                        went_over = True
                elif sum(computer_cards) >= 18:
                    computer_hitting = False
                    playing = False
        
elif want_to_play != 'y':
    print("Bye.")

if not went_over:
    if want_to_play == 'y':
        print(f'Opponent cards: {computer_cards} Total: {sum(computer_cards)}')
        if sum(player_cards) > sum(computer_cards):
            print(f'You win ${random.randrange(200,1000)}')
        elif sum(player_cards) < sum(computer_cards):
            print(f'You lose ${random.randrange(200,1000)}')
        else:
            print("It's a draw!")
# play_again = input('Do you want to play again: Type y or n')
# if play_again == True:
#     clear()
#     player_cards = []
#     computer_cards = []
    

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
