import random
from enum import IntEnum

class Action(IntEnum):
    rock = 1
    paper = 2
    scissors = 3
    lizard = 4
    spock = 5

def get_user_play():
    user_choice = input('Rock[1], Paper[2], Scissors[3], Lizard[4], Spock[5]: ')
    user_action = int(user_choice)
    action = Action(user_action)
    print('You chose:', action.name)
    return action

def get_computer_play():
    computer_choice = random.randint(1, 6)
    choice = Action(computer_choice)
    print('Opponent chose:', choice.name)
    return choice

def determine_winner(action, choice):
    win = f'{action.name} beats {choice.name}. You win!'
    lose = f'{choice.name} beats {action.name}. You lose!'
    draw = 'There was a tie!'
    
    wins = {
    Action.scissors: [Action.lizard, Action.paper],
    Action.paper: [Action.spock, Action.rock],
    Action.rock: [Action.lizard, Action.scissors],
    Action.lizard: [Action.spock, Action.paper],
    Action.spock: [Action.scissors, Action.rock]
    }

    losses = wins[action]
    if action == choice:
        print(draw)
    elif choice in losses:
        print(win)
    else:
        print(lose)
       
while True:
    action = get_user_play()
    choice = get_computer_play()
    determine_winner(action, choice)

    play_again = input('Play again? (y/n) ')
    if play_again == 'n':
        break
   
    
    



    
