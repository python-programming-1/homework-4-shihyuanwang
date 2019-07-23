# HW4 - rock paper scissors game - SHIH-YUAN WANG
#----------------------------------------------------------------------------------------------

import random
inputs = {'r': 'rock','p': 'paper','s': 'scissors'}

# decide who wins the game and returns score
def win_lose_tie(human, computer):
    computer_score = 0
    human_score = 0
    win_lose_tie = ''

    # computer wins
    if (human == 'r' and computer == 'p')\
        or (human == 'p' and computer == 's')\
        or (human == 's' and computer == 'r'):
        computer_score = 1
        win_lose_tie = 'lose'
        print('You chose ' + inputs[human] + ' and the computer chose ' + inputs[computer] + '. You '\
              + win_lose_tie + '!\n(Inputs "sc" to view scores or enters nothing to the next step.)')

    # player wins
    elif (computer == 'r' and human == 'p')\
        or (computer == 'p' and human == 's')\
        or (computer == 's' and human == 'r'):
        human_score = 1
        win_lose_tie = 'win'
        print('You chose ' + inputs[human] + ' and the computer chose ' + inputs[computer] + '. You '\
              + win_lose_tie + '!\n(Inputs "sc" to view scores or enters nothing to the next step.)')

    # draw
    elif (human == computer):
        win_lose_tie = 'Draw'
        print('You chose ' + inputs[human] + ' and the computer chose ' + inputs[computer] + '. '\
              + win_lose_tie + '!\n(Input "sc" to view scores or enters nothing to the next step.)')
    return human_score, computer_score

#--

# create dic move_count: user input as key and set 0 as the initial value (the number of corresponding input)
move_count = {'r': 0, 'p': 0, 's': 0}

# smarter computer move based on the player's history of moves
def computer_move(user_input):

    # for check: print('Before user input:', str(move_count), str(move_count[user_input]))

    max_value = max(move_count.values())  # maximum value

    # If the maximum value >= 3, predicted user input is randomly generated from key r/s/p
    # that has maximum value, and the computer generates the opposite win-choice.
    if max_value >= 3:
        # getting all keys containing the 'maximum'
        max_keys = [k for k, v in move_count.items() if v == max_value]
        input_keys = random.choice(max_keys)
    
        if input_keys == 'r':
            computer = 'p'
        elif input_keys == 'p':
            computer = 's'
        elif input_keys == 's':
            computer = 'r'

    # If the maximum value < 3, predicted user input is randomly generated from key r/s/p
    # , and the computer generates the opposite win-choice.
    else:
        computer = random.choice(list(move_count.keys()))

    move_count[user_input] += 1    # update the value upon this input
    # for check: print('After user input:', str(move_count), str(move_count[user_input]))

    return computer

#----

hum_score = 0
com_score = 0
total_hum_score = 0
total_com_score = 0
play_again ='y'

print('Welcome to Rock, Paper, Scissors Game!')

# Loop for user to play again
while (play_again == 'y'):
    print('Make a move! (r/s/p): ')
    human = str(input()).lower()

    # if user doesn't input r/s/p
    while human not in inputs:
        # if user inputs 'sc', prints out the score
        while human == 'sc':
            print('human: ' + str(total_hum_score) + ', computer: ' + str(total_com_score))
            human = str(input()).lower()
        else:
            if human not in inputs:
                print('You must enter "r" for rock, "s" for scissors, or "p" for paper.')
                human = str(input()).lower()

    # call computer_move() to return computer move
    computer = computer_move(human)

    # call win_lose_tie() to print out the result and return scores
    hum_score, com_score = win_lose_tie(human, computer)

    # calculate total scores
    total_hum_score += hum_score
    total_com_score += com_score

    # Print out total scores if user inputs 'sc'
    if input() == 'sc':
        print('human: ' + str(total_hum_score) + ', computer: ' + str(total_com_score))

    # promps for user input to play again
    print('Do you want to play again? (y/n) ')
    play_again = str(input()).lower()

    # if user doesn't input y/n
    while play_again not in ['y','n']:
        # if user inputs 'sc', prints out the score
        while play_again == 'sc':
            print('human: ' + str(total_hum_score) + ', computer: ' + str(total_com_score))
            play_again = str(input()).lower()
        else:
            if play_again not in ['y','n']:
                print('You must enter "y" for yes, or "n" for no.')
                play_again = str(input()).lower()

    # if user inputs 'y', restart the game
    if (play_again == 'y'):
        continue
    # if user inputs 'n', terminate the game
    elif (play_again == 'n'):
        print('Thanks bye!')
        break
