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

class HardworkingTrainee(Trainee):
    '''
    A subclass of Trainee representing a hardworking student who gets extra points.
    '''
    def __init__(self, name, surname, score = 0, passing_grade = 10):
        super().__init__(name, surname, score, passing_grade)

    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2

class AuditTrainee(Trainee):
    '''
    A subclass of Trainee representing an auditing student.
    '''
    def __init__(self, name, surname, score = 0, passing_grade = 10):
        super().__init__(name, surname, score, passing_grade)

    def is_passing(self):
        '''Always completes the course.'''
        return True

class Cohort:
    '''
    A class representing a study group (cohort) of trainees.

    Attributes:
        title (str): Name/identifier of the cohort
        trainees (list[Trainee]): List of Trainee objects in the group
    '''
    def __init__(self, title: str, trainees: list[Trainee] = None):
        self.title = title
        # Чтобы не использовался один и тот же список, а создавать разные для разных групп
        self.trainees = trainees if trainees is not None else []

    def add_trainee(self, trainee: list[Trainee]) -> None:
        '''
        Adds a trainee to the group.
        
        Args:
            trainee (Trainee): The trainee object to add to the cohort
        '''
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        '''
        Simulates conducting a lecture for all trainees in the cohort.
        '''
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        '''Returns a list of all trainees who have passed the course.'''
        # Генератор списка для возврата True
        return [trainee for trainee in self.trainees if trainee.is_passing()]

    
def main() -> None:
    # 1. Создаем учащихся разных типов
    std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
    hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
    audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0,passing_grade=10)

    # 2. Создаем группу и добавляем студентов
    cohort = Cohort("Python Advanced")
    cohort.add_trainee(std_trainee)
    cohort.add_trainee(hard_trainee)
    cohort.add_trainee(audit_trainee)

    # 3. Проводим лекцию для всей группы (+1 балл всем)
    cohort.conduct_lecture()

    # 4. Проверяем работу переопределенного ДЗ для трудоголика (+2  балла)
    hard_trainee.do_homework()

    # 5. Выводим список тех, кто проходит курс
    passing_students = cohort.get_passing_students()
    print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
    for student in cohort.trainees:
        print(f"{student.name:10} {student.surname:10} | Баллы: {student.score} | Проходит: {student.is_passing()}")

    print("\nУспешно зачислены на следующий модуль:")
    for student in passing_students:
        print(f"- {student.name} {student.surname}")

if __name__ == '__main__':
    main()

# В ходе тестов были справлены 
# - Ошибки в названии методов
# - Неправильно написанный оператор (=+), поэтому баллы счиатлись не верно