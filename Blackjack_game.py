import random
from blackjack_art import logo

def card_choice():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw🙂"
    elif c_score==0:
        return "lose, opponent have Blackjack😱"
    elif u_score==0:
        return "Win with Blackjack😎"
    elif u_score>21:
        return"Bust , You lose🙂‍↔️"
    elif c_score>21:
        return "Opponent went over, You win☺️"
    elif u_score>c_score:
        return "You win🥳"
    else:
        return "You lose😭"


def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over = False


    for _ in range(2):
        user_card.append(card_choice())
        computer_card.append(card_choice())

    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"your score{user_card} and score is:{user_score}")
        print(f"computer first card:{computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card or type 'n' to pass:").lower()
            if another_card == "y":
                user_card.append(card_choice())
            else:
                is_game_over = True

    while computer_score!=0 and computer_score<17:
        computer_card.append(card_choice())
        computer_score=calculate_score(computer_card)

    print(f"Your final hand:{user_card}, Your total score:{user_score}")
    print(f"Computer's final hand :{computer_card}, final score:{computer_score}")
    total=(compare(user_score,computer_score))
    print(total)
while input("Do you want to play a game of blackjack? Type 'y' or 'n'").lower() =='y':
    print("\n" * 20)
    play_game()
