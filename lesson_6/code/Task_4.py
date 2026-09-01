number = int(input('Введите целое число: '))
if number % 2 == 0:
    flag = 'чётное'
else:
    flag = 'нечётное'

print(f'Число {number} - {flag}')