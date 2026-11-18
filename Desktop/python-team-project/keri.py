# Класс для учёта успеваемости студента
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = []  # список оценок

    # Метод добавления новой оценки
    def add_grade(self, grade):
        self.grades.append(grade)

    # Метод вычисления среднего балла
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


# Функция вне класса для вывода информации о студенте
def print_student(student):
    print("=== Карточка студента ===")
    print("Имя:", student.name)
    print("Группа:", student.group)
    print("Оценки:", student.grades)
    print("Средний балл:", round(student.average_grade(), 2))


# Создание объекта и проверка работы
st = Student("Алексей", "ИВТ-101")
st.add_grade(5)
st.add_grade(4)
st.add_grade(5)
print_student(st)

