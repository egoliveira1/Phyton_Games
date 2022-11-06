def play_forca():
    print('********************************')
    print('Welcome to the Hanged game! ****')
    print('********************************')

    file = open('words.txt', 'r')
    words = []

    for line in words:
        line = line.strip()
        words.append(line)

    file.close()

    secret_word = 'banana'.upper()
    result = ['_' for letra in secret_word]
    number_of_letters = len(secret_word)

    hanged = False
    hits = False
    errors = 0

    print(result)
    print('The word has {} letters.'.format(number_of_letters))

    while(not hanged and not hits):
        print('Playing')

        trying = input('What is the letter? ')
        trying = trying.strip().upper()

        if(trying in secret_word):
            index = 0
            for letter in secret_word:
                if(trying == letter):
                    result[index] = trying
                index += 1
        else:
            errors += 1
            print('You made a mistake! You have {} more tries left.'.format(6-errors))

        hanged = errors == 6
        hits = "_" not in result
        print(result)

    if(hits):
        print('You win!')
    else:
        print('You lose!')

    print('Game over!')

if (__name__ == '__main__'):
    play_forca()