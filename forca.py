import random

def play_forca():
    welcome()
    secret_word = load_secret_word()
    result = start_results(secret_word)
    number_of_letters = len(secret_word)
    number_of_chances = 7
    print(result)
    print('The word has {} letters.'.format(number_of_letters))
    print('You have {} chances, good luck!'.format(number_of_chances))

    hanged = False
    hits = False
    errors = 0

    while(not hanged and not hits):
        print('Playing')

        trying = call_for_try()

        if(trying in secret_word):
            register_correct_try(secret_word, result, trying)
        else:
            errors += 1
            print('You made a mistake! You have {} more tries left.'.format(number_of_chances-errors))
            draw_hang(errors)

        hanged = errors == number_of_chances
        hits = "_" not in result
        print(result)

    if(hits):
        print_winner()
    else:
        print_loser(secret_word)

    print('Game over!')

def welcome():
    print('********************************')
    print('Welcome to the Hanged game! ****')
    print('********************************')

def load_secret_word():
    words = []

    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    position = random.randrange(0, len(words))
    secret_word = words[position].upper()
    return secret_word

def start_results(word):
    return ['_' for letra in word]

def call_for_try():
    trying = input('What is the letter? ')
    trying = trying.strip().upper()
    return trying

def register_correct_try(secret_word, result, trying):
    index = 0
    for letter in secret_word:
        if (trying == letter):
            result[index] = trying
        index += 1

def print_loser(secret_word):
    print("You lose!!!")
    print("The secret word was {}".format(secret_word))
    print("    _______________        ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\   ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/    ")
    print(" |   XXX       XXX   |     ")
    print(" |                   |     ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |       ")
    print("   | I I I I I I I |       ")
    print("   |  I I I I I I  |       ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_winner():
    print("Congratulations, you win!")
    print("       ___________       ")
    print("      '._==_==_=_.'      ")
    print("      .-\\:      /-.     ")
    print("     | (|:.     |) |     ")
    print("      '-|:.     |-'      ")
    print("        \\::.    /       ")
    print("         '::. .'         ")
    print("           ) (           ")
    print("         _.' '._         ")
    print("        '-------'        ")

def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'):
    play_forca()