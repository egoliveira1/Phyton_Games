import forca
import advinhacao

def choose_game():
    print('********************************')
    print('** Welcome! Choose your game. **')
    print('********************************')

    print('(1) Forca (2) Advinhação')

    game = int(input('What is your choice? '))

    if (game == 1):
        print('You choose Força')
        forca.play_forca()
    elif (game == 2):
        print('You choose Advinhação')
        advinhacao.play_advinhacao()

if (__name__ == "__main__"):
    choose_game()


