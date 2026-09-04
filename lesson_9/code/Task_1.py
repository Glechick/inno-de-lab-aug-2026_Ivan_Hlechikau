class Trainee:
    '''
    A class representing a trainee with a scoring system.
    
    Attributes:
        name (str): Trainee's first name
        surname (str): Trainee's last name
        passing_grade (int): Minimum score required to pass the course
        score (int): Private attribute storing the trainee's current score
    '''

    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self):
        '''
        Getter for the private __score attribute.
        
        Returns:
            int: Current score of the trainee
        '''
        return self.__score

    @score.setter
    def score(self, value):
        '''
        Setter for the private score attribute with validation.
        
        Args:
            value: New score value
            
        Raises:
            ValueError: If value is not an int or if value < 0
        '''
        if type(value) is not int:
            raise ValueError(f"Expected value of type int, got {type(value)}")
        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")

        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score += 1

    # Немного не понял, а если у человека счётчик пойдёт ниже нуля, как это будет обрабаываться, если score не может быть меньше 
    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        '''Comparison of the passing score and the current score.'''
        return self.__score >= self.passing_grade


def main() -> None:
    # 1. Создание стажера с начальным баллом 9 и проходным баллом 10
    trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

    print('=== ПРОВЕРКА УСПЕВВАЕМОСТИ СТАЖЁРА ===')

    # 2. Выполнение домашнего задания и проверка статуса 
    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 3. Пропуск лекции и проверка статуса
    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()

# Первый тест: забыл довать ещё одно _ для уровня доступа
# Второй тест поправил условие сравнения с > на >=