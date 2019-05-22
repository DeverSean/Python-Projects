#! Python3.7
# Simple ticTacToe game

import pprint

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printTheBoard(Board):
    print(Board['top-L'] + '|' + Board['top-M'] + '|' + Board['top-R'])
    print('- ' + '-' + ' -')
    print(Board['mid-L'] + '|' + Board['mid-M'] + '|' + Board['mid-R'])
    print('- ' + '-' + ' -')
    print(Board['low-L'] + '|' + Board['low-M'] + '|' + Board['low-R'])

theBoardList = list(theBoard.keys())

i = 0

while i < 9:
    printTheBoard(theBoard)
    print('Player ' + str(i%2 + 1) + ', choose among the following options:')
    print(theBoardList)
    playerChoice = input()
    if playerChoice in theBoardList:
        i += 1
        theBoardList.remove(playerChoice)
        if i%2:
            theBoard[playerChoice] = 'O'
        else:
            theBoard[playerChoice] = 'X'
    else:
        print(playerChoice + ' is not a valid option')
        
    x = 0
    o = 0
    for a in range(3):
        if theBoard[top-L] == 'X':
            x += 1
        elif theBoard[playerChoice] == 'O':
            o += 1
        if o == 3:
            print('Player 1 wins!')
        elif x == 3:
            print('Player 2 wins!')
    
            
            
        














    



    
     

























