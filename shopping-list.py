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
        new_items = input('> ').lower()

        if new_items == 'done':
            quit(shopping_list)
            break
        elif new_items == 'show':
            show_list(shopping_list)
            continue
        elif new_items == 'help':
            show_help()
            continue
        elif new_items == 'remove':
            show_list(shopping_list)
            idx = input('Which item? Tell me the number: ')
            remove_item(int(idx), shopping_list)
            continue
        else:
            new_list = new_items.split(',')
            index = input("Give position to insert, or hit enter to place at the end. ")
            if index:
                spot = int(index)
                for new_item in new_list:
                    shopping_list = add_new_item(new_item, shopping_list, spot)
                    spot += 1
            else:
                for new_item in new_list:
                    shopping_list = add_new_item(new_item, shopping_list, -1)

def print_list(list_x):
    for idx, x in enumerate(list_x):
        print('''{} : {}'''.format(idx, x))

def show_list(list_x):
    print('\nCurrent list:')
    print_list(list_x)
    print('\nKeep adding items:')

def quit(list_x):
    print('\nFinal list:')
    print_list(list_x)
    print('\nGoodbye!')

def show_help():
    print('\nSeperate each item with a comma!\n\nSpecial commands:\nDONE : quit the app\nSHOW : view the list\nREMOVE : delete an item\nHELP : help menu\n')

def add_new_item(x, list_x, index):
    if  index == -1:
        list_x.append(x)
        print('Added {}. List has {} items.'.format(x, len(list_x)))
    else:
        list_x.insert(index, x.strip())
    return list_x

def remove_item(idx, list_x):
    index = idx - 1
    item = list_x.pop(index)
    print("Removed: {}".format(item))

main()