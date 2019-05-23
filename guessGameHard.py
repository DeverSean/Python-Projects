import random
wins = 1
losses = 1


while True:
    possibleValues = [None]*20
    for i in range(21):
        possibleValues[i-1] = i
    tries = 4
    print('Guess the number between 1 and 20! You have 4 tries.')
    while True:

    #    for n in range(len(possibleValues)):
    #       print(str(possibleValues[n]))

        possibleValuesMax = possibleValues[len(possibleValues)-1]

        possibleValuesMin = possibleValuesMax - len(possibleValues)+1

        possibleValuesCenter = (possibleValuesMax + possibleValuesMin) / 2

    #    print('')
    #    print(possibleValuesMin,possibleValuesCenter,possibleValuesMax)

        guess = int(input())
        guess_persist = guess

        if len(possibleValues) == 1 and guess == possibleValues[0]:
            print('You win!!!!!! The answer was '+ str(guess))
            wins = wins+1
            #print('\rwins:'+str(wins)+' losses:'+str(losses)+'  ratio:'+str(wins/losses),end = '')
            break

        if guess == possibleValuesCenter-0.5 or guess == possibleValuesCenter or guess == possibleValuesCenter+0.5:
            if tries == 1 and len(possibleValues) == 2:
                possibleValues.remove(guess)
                guess = possibleValuesCenter
            elif guess in possibleValues:
                possibleValues.remove(guess)
                tilt = random.choice([-1,1])
    #            print(str(tilt))
                guess += tilt

        if guess > possibleValuesCenter:
            for i in range(guess,possibleValuesMax+1):
                possibleValues.remove(i)
            print('Guess is too high!')
        elif guess < possibleValuesCenter:
            for i in range(possibleValuesMin,guess+1):
                possibleValues.remove(i)
            print('Guess is too low!')

        tries = tries - 1
        if tries <= 0 and len(possibleValues) > 0:
            print('You lose! The answer was ' + str(random.choice(possibleValues)) + '.')
            losses = losses+1
            #print('\rwins:'+str(wins)+' losses:'+str(losses)+'  ratio:'+str(wins/losses),end = '')

            break
        else:
            print('You have ' + str(tries) + ' left.')
    print('Try again? (y/n)')
    sisyphus = str(input())
    if sisyphus == 'n':
        break
