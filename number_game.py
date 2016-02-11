import random

def main():

    secret_num = random.randint(1,10)
    welcome()

    while True:
        guess = int(input("> "))

        if guess == secret_num:
            print('Winner! My number was {}'.format(secret_num))
            break
        else:
            print('Not it! Guess again!')

def welcome():
    print('''#### Welcome to the Number Guesser ####\nGuess a number 1 through 10''')

main()