import random

comp_wins = 0
player_wins = 0

def win():
    print('Congratulations! You win')


def lost():
    print('Sorry! You lost')


def draw():
    print("It's a draw")

def choose_option():
    user_choice = input('Rock, Paper or Scissors?: ')
    if user_choice in ['Rock', 'rock', 'r', 'R']:
        user_choice = 'r'
    elif user_choice in ['Paper', 'paper', 'p', 'P']:
        user_choice = 'p'
    elif user_choice in ['Scissors', 'scissors', 's', 'S']:
        user_choice = 's'
    else:
        print('Please input the right choice')
    choose_option()
    return user_choice


def computer_option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = 'r'
    elif comp_choice == 2:
        comp_choice = 'p'
    else:
        comp_choice = 's'
    return comp_choice


while True:
    print('')
    user_choice = choose_option()
    comp_choice = computer_option()
    print('')

    if user_choice == 'r':
        if comp_choice == 'r':
            draw()
        elif comp_choice == 'p':
            lost()
            comp_wins +=1
        elif comp_choice == 's':
            win()
            player_wins +=1

    elif user_choice == 'p':
        if comp_choice == 'r':
            win()
            player_wins +=1
        elif comp_choice == 'p':
            draw()
        elif comp_choice == 's':
            lost()
            comp_wins +=1

    elif user_choice == 's':
        if comp_choice == 'r':
            lost()
            comp_wins +=1
        elif comp_choice == 'p':
            win()
            player_wins +=1
        elif comp_choice == 's':
            draw()

    print('')
    print('Player wins: ' + str(player_wins))
    print('Computer wins: ' + str(comp_wins))
    print('')

    user_choice = input('Do you want to replay? (y/n)')
    if user_choice in ['Y', 'y', 'Yes', 'yes']:
        pass
    elif user_choice in ['N', 'n', 'No', 'no']:
        break
    else:
        break
