# Rock Scissor Paper Game
# Available Moves
from random import randint

Moves = ['rock', 'scissor', 'paper']

computer = Moves[randint(0, 2)]
player = False

# Winning / Losing Message
P = ('Player Win!, Computer Lose!')
C = ('Computer Win!, Player Lose!')

print('Welcome Players')
while player == False:
    player = input('Enter rock/scissor/paper: ')
    player = player.lower()
    if player != 'done':
        if player == computer:
            print('Computer Moves: ', computer)
            print('TIE!')
        elif player == 'rock':
            if computer == 'scissor':
                print('Computer Moves: ', computer)
                print(P)
            elif computer == 'paper':
                print('Computer Moves: ', computer)
                print(C)
        elif player == 'scissor':
            if computer == 'paper':
                print('Computer Moves: ', computer)
                print(P)
            elif computer == 'rock':
                print('Computer Moves: ', computer)
                print(C)
        elif player == 'paper':
            if computer == 'rock':
                print('Computer Moves: ', computer)
                print(P)
            elif computer == 'scissor':
                print('Computer Moves: ', computer)
                print(C)
    else:
        print('Thank You For Playing')
        quit()
player = False
computer = Moves[randint(0, 2)]
