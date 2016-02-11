# Script Goals:
# Ask for new items
# Add new items
# Quit App
# Print out list

def main():
    shopping_list = []

    print('### Welcome to Python Shopping List ### \n\nWhat should we pick up at the store?')
    show_help()

    while True:
        new_item = input('> ').lower()

        if new_item == 'done':
            quit(shopping_list)
            break
        elif new_item == 'show':
            show_list(shopping_list)
            continue
        elif new_item == 'help':
            show_help()
            continue

        shopping_list = add_new_item(new_item, shopping_list)

def print_list(list_x):
    for x in list_x:
        print(x)

def show_list(list_x):
    print('\nCurrent list:')
    print_list(list_x)
    print('\nKeep adding items:')

def quit(list_x):
    print('\nFinal list:')
    print_list(list_x)
    print('\nGoodbye!')

def show_help():
    print('\nSpecial commands:\nDONE : quit the app\nSHOW : view the list\nHELP : help menu\n')

def add_new_item(x, list_x):
    list_x.append(x)
    print('Added {}. List has {} items.'.format(x, len(list_x)))
    return list_x

main()