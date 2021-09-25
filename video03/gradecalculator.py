# In Politeknik Brunei
# Distinction is 80 marks above
# Merit is 65 to 79 marks
# Pass is 50 to 64 marks
# Fail is below 50 marks
main_menu = ('(1) Grade calculator',
            '(2) Histories',
            '(3) Show First Five',
            '(4) Show Last Five',
            '(5) Clear Histories',
            '(q) Quit Application')
while True:
    for menu in main_menu:
        print(menu)
    user_input = input('Please choose option as stated in parenthesis: ')

    if user_input == 'q':
        break
    elif user_input == '1':
        user_input = input('Please input marks between 0 to 100: ')
        if user_input.isdigit():
            grade = ''
            marks = int(user_input)
            if marks >= 0 and marks <= 100:
                if marks >= 80:
                    grade = 'Distinction'
                elif marks >= 65 and marks < 80:
                    grade = 'Merit'
                elif marks >= 50 and marks < 65:
                    grade = 'Pass'
                else:
                    grade = 'Fail'
                print(f'Marks inputted is {marks}, grade is {grade}')
            else:
                print('Invalid input. Must be between 0 to 100')
        else:
            print('Invalid input. Must be numbers.')
    elif user_input == '2':
        print('--- Showing histories ---')
    elif user_input == '3':
        print('--- Showing first five ---')
    elif user_input == '4':
        print('--- Showing last five ---')
    elif user_input == '5':
        print('--- Clearing histories ---')
    else:
        print('Invalid option chosen.')
    print()
print('Bye')