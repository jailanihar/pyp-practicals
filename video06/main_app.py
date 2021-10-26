def add_pirate():
    print('### Adding Pirate ###')
    name = input('Input pirate name: ')
    health = input('Input pirate health: ')
    x = input('Input new pirate location x: ')
    y = input('Input new pirate location y: ')
    print(f'Pirate name: {name}, health: {health} at ({x}, {y}) coordinate')

def move_pirate():
    print('### Moving Pirate ###')
    x = input('Input current pirate location x: ')
    y = input('Input current pirate location y: ')
    new_x = input('Input new x location to move: ')
    new_y = input('Input new y location to move: ')
    print(f'Pirate at ({x}, {y}) coordinate moved to new coordinate ({new_x}, {new_y})')

menus = ('(1) Show Arena',
            '(2) Add Pirate',
            '(3) Move Pirate',
            '(q) Quit Application')

while True:
    for menu in menus:
        print(menu)
    user_input = input('Please select an option: ')

    if user_input.lower() == 'q':
        quit()
    
    if user_input.isdigit():
        option = int(user_input)
        if option == 1:
            print('Show Arena')
        elif option == 2:
            add_pirate()
        elif option == 3:
            move_pirate()
        else:
            print('Error: Invalid option range')
    else:
        print('Error: Invalid option')