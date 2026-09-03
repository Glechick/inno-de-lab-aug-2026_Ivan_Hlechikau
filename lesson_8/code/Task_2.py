from const import PERFORMANCE_LOG_PREFIX, TIME_DECIMALS
from time import perf_counter

def performance_logger(func: callable) -> callable:
    '''
    Декоратор для измерения времени выполнения функции и логирования результатов.
    
    Декоратор замеряет время выполнения целевой функции с помощью time.perf_counter(),
    выводит сообщение в консоль с временем выполнения и возвращает результат функции.

    Args:
        func (callable): Целевая функция, время выполнения которой необходимо измерить.
    
    Returns:
        callable: Обернутая функция, которая выполняет замер времени и логирование.
    '''
    def wrapper (*args: any, **kwargs: any) -> any:
        """
        Внутренняя функция-обертка, выполняющая замер времени.
        
        Args:
            *args (any): Позиционные аргументы целевой функции.
            **kwargs (any): Именованные аргументы целевой функции.
        
        Returns:
            any: Результат выполнения целевой функции.
        """
        start_time = perf_counter()

        result = func(*args, **kwargs)

        print(f'{PERFORMANCE_LOG_PREFIX} Функция "{func.__name__}" выполнена за {(perf_counter() - start_time):.{TIME_DECIMALS}f} сек.')
        return result
    return wrapper

@performance_logger
def get_sorted_report (data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    '''
    Сортирует отчёт по выручке в порядке убывания.

    Функция принимает список словарей с данными о выручке по жанрам
    и сортирует его по ключу 'total_sales' от наибольшего к наименьшему
    с использованием lambda-выражения.

    Args:
        data (list[dict[str, str | float]]): Cписок словарей.
    Returns: 
        list[dict[str, str | float]]: Отсортированный по убыванию total_sales список.
    '''
    sorted_data = sorted(data, key=lambda x: x['total_sales'], reverse=True)
    
    return sorted_data

def main():
    '''
    Главная функция тестирования
    '''

    test_data_sets = [
        [
            {"category": "Action", "total_sales": 4311.85},
            {"category": "Animation", "total_sales": 4656.30},
            {"category": "Children", "total_sales": 3655.55}
        ],
                
        [
            {"category": "Classics", "total_sales": 1200.10},
            {"category": "Comedy", "total_sales": 4000.00},
            {"category": "Documentary", "total_sales": 4000.00}
        ],
        
        [
            {"category": "Drama", "total_sales": 500.00}
        ]
    ]

    print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

    # Цикл по количеству списков в списке
    for test_num, data in enumerate(test_data_sets, start=1):
        print(f'\n--- TECT {test_num} ---')

        # Вызов функции
        sorted_result = get_sorted_report(data)

        print("Топ категорий по выручке:")
        # Цикл по количеству словарей в списке
        for i, item in enumerate(sorted_result, start=1):
            print(f'{i}. {item['category']}: {item['total_sales']}')

if __name__ == "__main__":
    main()
    