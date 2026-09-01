first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
operator = input('Выберите оператор (+, -, *, /): ')

if operator == '+':
    print(f'Результат: {first_number} '
            f'{operator} {second_number} = '
            f'{first_number + second_number}')
elif operator == '-':
    print(f'Результат: {first_number} '
            f'{operator} {second_number} = '
            f'{first_number - second_number}')
elif operator == '*':
    print(f'Результат: {first_number} '
            f'{operator} {second_number} = '
            f'{first_number * second_number}')
elif operator == '/':
    if second_number == 0:
        print('Деление на ноль!')
    else:
        print(f'Результат: {first_number} '
                f'{operator} {second_number} = '
                f'{first_number / second_number}') 
else:
    print('Введён не верный оператор!')  
