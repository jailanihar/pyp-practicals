# In Politeknik Brunei
# Distinction is 80 marks above
# Merit is 65 to 79 marks
# Pass is 50 to 64 marks
# Fail is below 50 marks
while True:
    user_input = input('Type marks between 0 to 100: ')

    if user_input == 'q':
        break

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
print('Bye')