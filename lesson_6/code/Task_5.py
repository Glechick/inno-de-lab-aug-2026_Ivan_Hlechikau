from random import randint

# Константы и переменые для значий которые можно менять
START = 1
STOP = 20

hidden_number = randint(START, STOP)
attempts = 5
user_attempts = 0

print(f'Я загадал число от {START} до {STOP}. '
      f'У тебя {attempts} попыток!\n'
      'Выход "-1"')

while(attempts > 0):
    user_attempts += 1
    user_number = int(input(f'Попытка {user_attempts}. Введите число: '))
    attempts -= 1
    # Преждевременный выход
    if user_number == -1:
        print('Выход')
        break
    elif user_number == hidden_number:
        print('Ты угадал! Отличная работа.')
        break
    elif user_number > hidden_number:
        print(f'Слишком много! Осталось попыток:  {attempts}')
    else: 
        print(f'Слишком мало! Осталось попыток: {attempts}')
else:
    # Если попытки у пользователя закончились
    print(f'Попытки закончились! Было загадано число {hidden_number}')

