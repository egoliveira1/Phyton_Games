def play_forca():
    print('********************************')
    print('Welcome to the Hanged game! ****')
    print('********************************')

    secret_word = 'banana'
    result = ['_', '_', '_', '_', '_', '_']
    number_of_letters = len(secret_word)

    hanged = False
    hits = False

    print(result)
    print('The word has {} letters.'.format(number_of_letters))

    while(not hanged and not hits):
        print('Playing')

        trying = input('What is the letter? ')
        trying = trying.strip()

        index = 0

        for letter in secret_word:
            if(trying.upper() == letter.upper()):
                result[index] = trying
            index = index + 1
        print(result)

    print('Game over!')

if (__name__ == '__main__'):
    play_forca()