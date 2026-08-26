# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
# Ваш код здесь

# Генератор списков и очистка от пробелов
clean_strings = [item.strip() for item in raw_user_record.split(';')]

# Не особо понял то ворматирование или нет, но в лекции есть форматирование f-строкой
print(f'UID-{clean_strings[0]}')

# Или полностью изменить
# Преобразование имени
# Перевод названиея города к верхнему регистру
clean_strings = [
    f'UID-{clean_strings[0]}',
    clean_strings[1].replace('_', ' ').title(),
    clean_strings[2].upper(),
    clean_strings[3].lower(),
]

final_string = ' | '.join(clean_strings)

print(f'Нормализованная запись: {final_string}')