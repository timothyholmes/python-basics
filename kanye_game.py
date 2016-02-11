import os
import sys
import random

words = [
    'dropout',
    'registration',
    'graduation',
    'heartbreak',
    'fantasy',
    'yeezus',
    'pablo'
]

## Function that clears the window based on OS
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('\nStrikes: {}/7\n'.format(len(bad_guesses)))

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')

    print('\n')

def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input('Guess a letter: ')
        if len(guess) > 1:
            print('Too many letters!')
        elif len(guess) < 1:
            print('You have to pick a letter!')
        elif guess in bad_guesses or guess in good_guesses:
            print('You already used that!')
        elif not guess.isalpha():
            print('You can only guess letters!')
        else:
            return guess.lower()

def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True

            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print('You win!')
                print('The secret was {}'.format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print('You lost')
                print('Secret word {}'.format(secret_word))
                done = True

        if done:
            play_again = input('play again? Y/n ').lower()
            if play_again == 'n':
                sys.exit()
            else:
                return play(False)
                
def welcome():
    draw_ye()
    start = input('### Welcome to KanYe Album Guess ###\nPress enter to start, Q to quit')

    if start.lower() == 'q':
        print('Bye!')
        sys.exit()
    else:
        return True

def main():
    while True:
        clear()
        welcome()
        play(False)

# Shoutout http://www.flipmytext.com/ascii/hiphopartists.php for  the ASCII art
def draw_ye():

    kanye_west = '''
:  ....,.......,..,...  ..,,,.,:::~::::::::+~=~:,,., ..,,.,.,:,,,.,,..........+Z
....... ...,,..,...........,~OOOO88N$$$ZO$$$$$$7=,...........~:,,...,.........,Z
.. .........~.........,:=$8DMNDD8DNNDNDDDNNDDNNDZI+:.......,...................,
....................,~7ODDDMD8ODNNNDDD88ND8DDNNDNNO?:,.,,,,,. ..,:... .........:
..................,=$MNDDDDDDDD8O88DND8OO88OD8DMNNNNI~,...,,,........  ..... .~?
...............,,~?NDN8DN8O$$Z77I?IIIII777$$Z8DNDDNDN7=:....,.............. ..+I
.................$DDDNDDO$$$77IIIIIIII?I??IIII7$$Z7ODN7+.................  .. .,
................?8NDNDDOZ7$777II???III?????III77$$Z$Z88I~............. ..  .....
.... ..........,DNDNDD8Z$77777III?+++???????II777$$ZOO87~....... ... ..........,
 .............,~DNNDD8OZ77$77II????=++++?++??I7777$ZZO8D~,,.,.. ....... .......:
...... ...,...:$NDDD8OO$7$7$77I??+~+====?=IIIII77$$ZOO8O+,..... ....:. .. ......
...... ...,...=ZNNNN88OZ$777$7I?I++==+++++=??+??I7$ZZOOO7...,......:............
....... ......:DNDNDD8O$$$$$$77I??+===+?+I??II?II77ZZZOO8,.. .,......... .......
.........,.. .:8NDDDDDZ$7$$$$7???+==~~~==?????+??I7$ZZOOO+...::,...............:
..... ........~7NNDD8O$$$ZZZ777O7$$$Z$7?+~~=++?+II7$$ZZOO=, ..,,,.....:... . ..?
....  .. .....~7DDDD8Z$$$Z8MNMMNNMMMNMMMMMNND8DNNMMMMMMNMN7I?...,... .~.. ....,=
..............+?ZDDD8OZ$ZNMMMMMMMMMNMMNMMMMNMMMMMMMMMMMMMNMMM~...... ,........,=
.. . .........,=ZDD8OZZ$$MNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMI=..,.    .  .   . .
. . . .  .....,INNDNMMNMNNMMMMMMMMMMMMMMMMD~MMNMMMMMMMMMMMDMDI.....             
..   .......,=Z77ODDOO$ZZMMMMMMMMMMNMMMMNMM$?$DMMMMMMMMMMNNMN~...,.. ..  ......,
.    ........:D8$I7OOZZ$$MNMMMMMMMMMMMNMMMZ?+IOMMMMMMMMMMNMM7?.....   .  .......
..   ........+$$777ZOZZ$$MNMMMNNNNNNMNMMMN?+?I$NMMMMMMMMMNMZ?~....    ...   ....
. .  ........~I7IOZ$OZ$$$MNMNNNNNNMNNNMMM7?+??$OMMMMMMMMMMM?=... .  . ... ..  .~
.    ........~III$$7ZOZ$7$DMMNNNNNNNNNND$II???IZ8MMMMMMMMMM=.,....   ..  .... .Z
... ..... ...~?I?=7Z$OZ$$7III$ZZZOOOOODI???+~:?7Z$ODDNMMMN+.... .  .... .  . ...
....... .....~77??7$OZZZ$7III?++++++++7II7ZZ$7Z8OZOODDDND8=.... ... ...       ..
...  . .,,...:II$$Z$OZZZ$777??++==++++$8NMOOMMMMNDZ$$$ZOO?....... ..,,..     . .
. . . ........:+I7I7OZ$Z$$77I??+++????III$IZ7788OZZZ$$ZOO+..,,.. .........  ....
. ... .........,:=$8OZZ$$$777IIII?I?+??$$$I?ZZ788O$$Z$ZOOI,......  .......  . ..
... .............:~Z8Z$$$777777I7I+?O$7+I7I?77$$$88ZZOOO8=,,..,,... ...... .....
... . ......,~.....~ZOZ$$$777777$7?7Z7OOZOZZ7ZO8OOOOZOOOZ,.....,:,. ....,.....:I
..  ........,,.....,ZOZZ$7$777777778DOII?I??I??ZNN88ZOOZ?,:...,.. .....,...  .?Z
+,..........:.... .,ZZOZZ$$$$$777$ZI??I?????I?7$ZZ7$ZO$I:,.. ..,... ....,. ...$O
..... ... .........:ZZZ8OZZZ$$$$7$ZI?III77O88DD8$Z$$O$=:.,....,,=~............,7
.. ... ..... ....,::ZZZZ8OOZZZZ$OO87$7$777I787ZZOOO8O$?,,. .,O7+:,......,.....,=
... ........:...,=~NOZ$ZZ888OZOZZO8ZZZ$$$$ZOZ8O88DNDDDDO..I?77~:......,,:.... .?
..........,OI.,,:NM8OZZ$ZOONDO8OZOD$$Z7777I7ZZOO8DNNMMMND$OIO,.............. .:+
.  .... ......::NMNMOZZ$$ZO8DMD88ODOD888ZO8ZDD88NMMMMN8D++7M?~...,,,..:,......=I
.............,DDNOZM8ZZZ$$ZZODMNDO88ODODO88DDDNNMMMND8O7$NMNN:...,,...........~I
.....,......,NDNDOZ8DZ$ZZ$ZZZOOOMM8NDNN88O8DNNNNMMNO877ZOMNMNN.,..... .......,,?
~. .......,:DDDDDDD+8Z$$$ZZZZZOZZZMMMMMMMMMMNMMMM8OO8NNNNMMNMNN+~.............:+
.. ......,+DDDDNDDD88O$$$77$ZZOZOOZDMMMMMMMMMMMMOOZO8NMMMDMNNNDN7=,,..........:+
..,.. .,.ZDDDDDND88N8OZ$$77$Z$ZOOOOOONMMMMMMMMMOZZOO8NMN88MNNNNNNNN$=~:......,,=
.......:ODDDDDNODD8D8OZ$$$$$7$ZOOOO888DMMMMMMMOZOOOOD8NNIDMNDNNNNNNNZ8?:.. . ..=
..  .+O8DDNDDDO8DDD8DDZ$$$$77$$ZZOO888DDDMMMNOZZZOOOM+NMDD8NNDNNDNNDNDODD$+,....
...:7Z8DDDDDDDDDDDDO88=$$$$$7777$Z$ZO8OOOZZZZZZZZOONMDDN$$DMNDDNNNDDDDD8DDD8=,,,
?$ZO8DDDDDNDDDNDDND7$888Z$$$$$77$$$$$$$$$$777$ZZONNM$DDN$Z7MDDNNNNNN8DDDDDDD8ZII
D88DD8DDDDDNDDNDDNN8D88DD88$$$7$7$$$$$7$7777$8NNNNNZ88DM$DOMNDNNNNNNDDDDNNDDNDN8
DDDD8DDDDNNDDDN88NN8DN8:$888Z$$77777$77$8DDNNNNNNNN~DDNNDNMMNDDNNNNNDNDDDNNDDDND
DDD8NDDNDNDNDNND8DM?8D+OI~OD88D8DDNDDNNNNNNNNNNNDDZDDDNN=NDDMDNNNNNNNNDNDDNDDNDD
DDDNDNDDDNNDDDND88D788N?~D88888O8DNNDDNDDDNDDDDDDND8DD8I?DDOMNNNNNNNDNNDNDDND8DD
DDDDDDDDNDNNNDDD88D$DDDD8DD8788888DDDDDDDDDDDDDDDNDD8D:D8D?IMDDNNNNNNNDDNDDDNDDD
DNDDNDDDNDNNDDDD888=DI$DND8$ZI788888ZZDDDD8DDD8DDDD8DN8DDD8NMNNNNNNNDNNNDDNDN88D
DNNNDDDDDNNNNDDD888=D788DMNN7O888DD888Z8DDDDDDDDNDDDDD,~8DDDMMNNNNNNNNNDDDDNDZD8
DDDDDDDDDDNNDDDD8888DND+8DMNDDDDDZZ88D8888DDDDDDDDD:8D7+D8DZMMDNNNNNNNDDDDD888O$'''

    print(kanye_west)

main()