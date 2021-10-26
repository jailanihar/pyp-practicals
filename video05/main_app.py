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
            print('Adding Pirate')
        elif option == 3:
            print('Moving Pirate')
        else:
            print('Error: Invalid option range')
    else:
        print('Error: Invalid option')