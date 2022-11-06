import random

def play_advinhacao():
    print('********************************')
    print('Welcome to the Guessing Game! **')
    print('********************************')

    secret_number = random.randrange(1, 101)
    chances = 0
    points = 1000

    print('Difficult level')
    print('(1) Easy (2) Normal (3) Hard')

    level = int(input('Choose your level: '))

    if (level == 1):
        chances = 20
    elif (level == 2):
        chances = 10
    else:
        chances = 5

    '''
    # Using a while loop
    nr_round = 1
    
    while (nr_round <= chances):
        print('Try {} of {}'.format(nr_round, chances))
        trying = input('Input a number between 1 and 100: ')
        trying = int(trying)
        print('You inputted:', trying)
    
        winner = secret_number == trying
        bigger = secret_number < trying
        smaller = secret_number > trying
    
        if (winner):
            print('You win!')
            break
        else:
            if (bigger):
                print('Your input was bigger then secret number, try again.')
            elif (smaller):
                print('Your input was smaller then secret number, try again.')
    
        nr_round = nr_round + 1
    '''
    # Using a for loop
    for nr_round in range(1, chances + 1):
        print('Try {} of {}'.format(nr_round, chances))
        trying = input('Input a number between 1 and 100: ')
        trying = int(trying)
        print('You inputted:', trying)

        if (trying < 1 or trying > 100):
            print('The number should be between 1 and 100!')
            continue

        winner = secret_number == trying
        bigger = secret_number < trying
        smaller = secret_number > trying

        if (winner):
            print('You win and your score was {}!'.format(points))
            break
        else:
            if (bigger):
                print('Your input was bigger then secret number, try again.')
            elif (smaller):
                print('Your input was smaller then secret number, try again.')
            lostpoints = abs(secret_number - trying)
            points = points - lostpoints

    print('Game over')

if (__name__ == "__main__"):
    play_advinhacao()

