# Script Goals:
# Ask for new items
# Add new items
# Quit App
# Print out list

def main():
    shopping_list = []

    start_message = 'What should we pick up at the store?\nPrint SEE to view the list\nPrint DONE to stop adding items.'

    print(start_message)

    while True:
        new_item = input().lower()

        if new_item == 'done':
            print('\nFinal list:')
            print_list(shopping_list)
            print(new_item)
            break
        elif new_item == 'see':
            print('\nCurrent list:')
            print_list(shopping_list)
            print('\nKeep adding items:')
        else:
            shopping_list.append(new_item)

def print_list(print_this):
    for x in print_this:
        print(x)

main()