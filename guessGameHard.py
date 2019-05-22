import random
    


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
        
        if guess == possibleValuesCenter or guess == 10:
            if guess in possibleValues:
                possibleValues.remove(guess)
            tilt = random.choice([-1,1])
            guess += tilt

        if guess == 15 and tries == 3:
            if guess in possibleValues:
                possibleValues.remove(guess)
            tilt = random.choice([-1,1])
            guess += tilt

        if guess == 5 and tries == 3:
            if guess in possibleValues:
                possibleValues.remove(guess)
            tilt = random.choice([-1,1])
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
        if tries <= 0:
            print('You lose! The answer was ' + str(possibleValues[0]) + '.')
            break
        else:
            print('You have ' + str(tries) + ' left.')
    print('Try again? (y/n)')
    sisyphus = str(input())
    if sisyphus == 'n':
        break
        
