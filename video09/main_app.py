from map import map
from pirate import pirate
import random as rand

m = map(7, 8)
for iter in range(0, 10):
    x = rand.randint(0, 6)
    y = rand.randint(0, 7)
    p = pirate()
    m.add_pirate(x, y, p)

def input_digit(s):
    while True:
        input_digit = input(f'{s}')
        if input_digit.isdigit():
            return int(input_digit)
        print('Error: Must be digit')

def add_pirate():
    print('### Adding Pirate ###')
    name = input('Input pirate name: ')
    health = input_digit('Input pirate health: ')
    x = input_digit('Input new pirate location x: ')
    y = input_digit('Input new pirate location y: ')
    m.add_pirate(x, y, pirate(name, health))
    print(m)

def move_pirate():
    print('### Moving Pirate ###')
    x = input_digit('Input current pirate location x: ')
    y = input_digit('Input current pirate location y: ')
    new_x = input_digit('Input new x location to move: ')
    new_y = input_digit('Input new y location to move: ')
    m.move_pirate(x, y, new_x, new_y)
    print(m)

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
            print(m)
        elif option == 2:
            add_pirate()
        elif option == 3:
            move_pirate()
        else:
            print('Error: Invalid option range')
    else:
        print('Error: Invalid option')