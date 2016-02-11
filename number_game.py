import random

def main():

    secret_num = random.randint(1,10)
    guesses = []

    welcome()

    while len(guesses) < 5:
        try:
            guess = int(input("> "))
        except ValueError:
            print('{} is not a number!'.format(guess))
        else:
            if guess == secret_num:
                print('Winner! My number was {}'.format(secret_num))
                break
            elif guess > secret_num:
                print('{} is too high! Guess again!'.format(guess))
            else:
                print('{} is too low! Guess again!'.format(guess))

            
            guesses.append(guess)
    else:
        print('You lost! Secret number was {}'.format(secret_num))

    play_again = input('Do you want to play again? Y/n').lower()

    if play_again != 'n':
        main()
    else:
        print('Goodbye!')


def welcome():
    print('''\n\n#### Welcome to the Number Guesser ####\nGuess a number 1 through 10\n\n''')

main()