from const import DEFAULT_RETURN_INDEX_BASE

def calculate_overdue_fine (film_name: str, days_overdue: any, fine_rate: float) -> tuple[float, float] | None:
    '''
    Рассчитывает штраф и технический индекс оборачиваемости.

    Функция обрабатывает различные ошибки входных данных:
    - TypeError: при передаче некорректного типа данных (например, список)
    - ValueError: при передаче строки, которую нельзя преобразовать в число
    - ZeroDivisionError: при передаче 0 дней просрочки
    - Другие исключения: перехватываются и выводят общее сообщение об ошибке

    Args:
        film_name (str): Название фильма для логирования ошибок.
        days_overdue (Any): Количество дней просрочки (может быть int, float, str или list).
        fine_rate (float): Стоимость штрафа за один день просрочки.

    Returns:
        Tuple[float, float]: Кортеж (total_fine, return_index) при успешном расчете,
        или None в случае ошибки.
            - total_fine (float): Общая сумма штрафа
            - return_index (float): Технический индекс оборачиваемости
    '''
    try:
        numeric_days = float(days_overdue)

        total_fine = numeric_days * fine_rate
                 
        return_index = DEFAULT_RETURN_INDEX_BASE /numeric_days

        # Успешный расчет
        print(f'Фильм: "{film_name}" | Итоговый штраф: {total_fine:.1f}$ | Индекс: {return_index:.1f}')
        return total_fine, return_index

    except TypeError as e:
        print(f'[ОШИБКА ТИПА] Некорректный тип данных для "{film_name}": {e}')
        return None
    
    except ValueError as e:
        print(f'[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для "{film_name}": {e}')
        return None
    
    except ZeroDivisionError as e:
        print(f'[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для "{film_name}": {e}')
        return None

    except Exception as e:
        print(f'Неизвестная ошибка для "{film_name}": {e}')
        return None
    
    finally:
        print('--- Проверка транзакции возврата завершена ---')


def main():
    '''
    Главная функция тестирования
    '''

    data = [
        {
            "name": "Matrix",
            "days": 5,
            "rate": 1.5,
            "expected": "Успешный расчет"
        },
        {
            "name": "Inception",
            "days": "пять",
            "rate": 2.0,
            "expected": "ValueError"
        },
        {
            "name": "Avatar",
            "days": 0,
            "rate": 2.5,
            "expected": "ZeroDivisionError"
        },
        {
            "name": "Interstellar",
            "days": [3],
            "rate": 3.0,
            "expected": "TypeError"
        }
    ]

    print("=== ПРОВЕРКА ВОЗВРАТОВ ===\n")

    for test in data:
        calculate_overdue_fine(test['name'],
                               test['days'],
                               test['rate'])
        print()

if __name__ == '__main__':
    main()