from const import MAX_RENTAL_BATCH_LIMIT

def calculate_wholesale_batch (quantity: int, rental_rate: float, discount: float = 0) -> tuple[float, bool]:
    '''
    Рассчитывает стоимость партии дисков для оптовой аренды с учетом скидки и проверяет превышение установленного лимита.

    Args:
        quantity (int): Количество дисков.
        rental_rate (float): Стоимость аренды одного диска.
        discount (float, optional): Проценты скидки. Поумолчанию 0.
    Returns:
        Tuple[float, bool]: Кортеж, содержащий:
            final_sum (float): Итоговая стоимость аренды.
            is_limit_exceeded (bool): True, если сумма превышает лимит, иначе False.
    '''

    final_sum = round(quantity * rental_rate * (1 - discount), 2)

    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exceeded

def main():
    '''
    Главная функция тестирования
    '''
    
    test_batches = [
        ("Academy Dinosaur", 30, 2.99, 0.0),
        ("Affair Prejudice", 40, 4.99, 0.1),
        ("Agent Truman", 10, 1.99, 0.0),
        ("African Egg", 50, 3.50, 0.2),
    ]

    print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===\n")

    # Посмотрел способ с enumerate для красивого вывода номера, также можно сделать через range(len())
    for i, (title, qty, rate, disc) in enumerate(test_batches, start=1):
        final_sum, is_limit_exceeded = calculate_wholesale_batch(
            quantity=qty, 
            rental_rate=rate, 
            discount=disc)
        print(f'Партия {i} {title}: Сумма {final_sum}$. Превышение лимита: {is_limit_exceeded}')


if __name__ == "__main__":
    main()