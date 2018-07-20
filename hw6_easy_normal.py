import math

# Задача-1: Написать класс для фигуры-треугольника,
# заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# Пример использования класса треугольника:


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def length(p1, p2):
        length = math.sqrt((p1[0] - p2[0])**2 +
                           (p1[1] - p2[1])**2)
        return length

    def height_a(self):
        return 2 * self.square / self.length(self.a, self.b)

    def height_b(self):
        return 2 * self.square / self.length(self.b, self.c)

    def height_c(self):
        return 2 * self.square / self.length(self.a, self.c)

    def perimeter(self):
        p = self.length(self.a, self.b) + self.length(self.a, self.c) + \
            self.length(self.b, self.c)
        return p

    @property
    def square(self):
        return math.fabs((self.a[0]-self.c[0])*(self.b[1]-self.c[1]) -
                         (self.b[0] - self.c[0])*(self.a[1] - self.c[1])) * 1/2

    def __str__(self):
        return "Triangle with coordinats: {} {} {}".format(self.a,
                                                           self.b,
                                                           self.c)


tr_1 = Triangle((1, 2), (7, 9), (5, 0))
print(tr_1)
print('Площадь:', tr_1.square)
print('Высота к стороне a:', tr_1.height_a())
print('Высота к стороне b:', tr_1.height_b())
print('Высота к стороне c:', tr_1.height_c())
print('Периметр:', tr_1.perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы для:
#  - проверки, является ли фигура равнобочной трапецией;
#  - вычисления: длины сторон, периметр, площадь.

# Пример использования класса трапеции:

class Trapezoid:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @staticmethod
    def line_equation(p1, p2):
        coefficient_x = (p2[1] - p1[1]) / (p2[0] - p1[0])
        constant = (p2[0]*p1[1] - p2[1]*p1[0]) / (p2[0] - p1[0])
        return {'x': coefficient_x, 'const': constant}

    def is_isosceles(self):
        len_ac = Triangle.length(self.a, self.c)
        len_bd = Triangle.length(self.b, self.d)
        return len_ac == len_bd

    def sides(self):
        len1 = Triangle.length(self.a, self.b)
        len2 = Triangle.length(self.b, self.c)
        len3 = Triangle.length(self.c, self.d)
        len4 = Triangle.length(self.d, self.a)
        return len1, len2, len3, len4

    @property
    def square(self):
        if self.line_equation(self.a, self.b)['x'] == self.line_equation(self.c, self.d)['x']:
            bases = [(self.a, self.b), (self.c, self.d)]
        else:
            bases = [(self.a, self.d), (self.b, self.c)]
        # ax + by +c = 0
        x1 = bases[1][0][0]
        y1 = bases[1][0][1]
        x2 = bases[1][1][0]
        y2 = bases[1][1][1]
        a = y2 - y1
        b = x2 - x1
        c = x1*y2 - x2*y1
        x0 = bases[0][0][0]
        y0 = bases[0][0][1]
        h = math.fabs(a*x0 + b*y0 + c) / math.sqrt(a**2 + b**2)
        side1 = Triangle.length(bases[0][0], bases[0][1])
        side2 = Triangle.length(bases[1][0], bases[1][1])
        s = h * (side1 + side2) / 2
        return s

    def perimeter(self):
        return sum(self.sides())

    def __str__(self):
        return "Trapezoid with coordinates: {} {} {} {}".format(self.a, self.b, self.c, self.d)

trap_1 = Trapezoid((0, 0), (1, 2), (3, 2), (4, 0))
trap_2 = Trapezoid((0, 0), (1, 2), (3, 2), (6, 0))
trap_3 = Trapezoid((0, 0), (1, 3), (3, 3), (9, 0))
traps = [trap_1, trap_2, trap_3]

for trap in traps:
    print(trap)
    if trap.is_isosceles():
        print('Равнобочная')
    else:
        print('Неравнобочная')    
    print('Длины сторон:', trap.sides())
    print('Площадь:', trap.square)
    print('Периметр:', trap.perimeter())

#Normal

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname, patronymic, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date
    def get_full_name(self):
        return self.name + ' ' + self.surname + ' ' + self.patronymic
    def get_surname_initials(self):
        return self.surname + ' ' + self.name[0] + '.' + self.patronymic[0] + '.'
    def set_name(self, new_name):
        self.name = new_name

class Teacher(Person):
    def __init__(self, name, surname, patronymic, birth_date, school, teach_subject):
        Person.__init__(self, name, surname, patronymic, birth_date)
        self.school = school
        self.teach_subject = teach_subject

class Class_room:
    def __init__(self, class_room, teachers):
        self._class_room = {'class_num': int(class_room.split()[0]), 'class_char': class_room.split()[1]}
        self.teachers_dict = {t.teach_subject: t for t in teachers}

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

class Student(Person):
    def __init__(self, name, surname, patronymic, birth_date, school, class_room, parents):
        Person.__init__(self, name, surname, patronymic, birth_date)
        self.school = school
        self.class_room = class_room
        self.parents = parents

    def next_class(self):
        self._class_room['class_num'] += 1

teachers = [Teacher('Анна', 'Крикова', 'Александрова', '11.11.1980', '2 лицей', 'математика'),
            Teacher('Любовь', 'Васильева', 'Анатольевна', '11.11.1980', '2 лицей', 'русский язык'),
            Teacher('Екатерина', 'Федорова', 'Ивановна', '11.11.1980', '2 лицей', 'литература'),
            Teacher('Любовь', 'Иванова', 'Викторовна', '11.11.1980', '2 лицей', 'математика'),

            Teacher('Надежда', 'Львова', 'Васильевна', '10.05.1977', '8 гимназия', 'русский язык'),
            Teacher('Петр', 'Николаев', 'Анатльевич', '18.02.1971', '8 гимназия', 'математика'),
            Teacher('Сергей', 'Егоров', 'Петрович', '19.09.1970', '8 гимназия', 'русский язык'),
            Teacher('Анна', 'Сергеева', 'Андреева', '11.10.1982', '8 гимназия', 'литература')]

class_rooms = [Class_room('5 А', [teachers[0], teachers[1], teachers[2]]),
              Class_room('7 А', [teachers[3], teachers[1], teachers[2]]),
              Class_room('3 Д', [teachers[5], teachers[4], teachers[2]]),
              Class_room('5 В', [teachers[5], teachers[6], teachers[7]])]

parents = [Person("Павел", "Алевсеев", "Сергеевич", '12.11.1979'),
           Person("Инна", "Александрова", "Павловна", '03.11.1979'),
           Person('Петр', 'Николаев', 'Анатльевич', '18.02.1971'),
           Person('Анна', 'Сергеева', 'Андреева', '11.10.1982')]

students = [Student("Александр", "Иванов", "Андреевич", '10.11.1998', "2 лицей", class_rooms[0], [parents[0], parents[1]]),
            Student("Петр", "Сидоров", "Александрович", '10.01.2004', "2 лицей", class_rooms[0], [parents[0], parents[1]]),
            Student("Анна", "Андреева", "Петровна", '12.11.1999', "2 лицей", class_rooms[1], [parents[2]]),
            Student("Иван", "Петров", "Александрович", '10.11.1999', "2 лицей", class_rooms[1], [parents[0], parents[1]]),
            Student("Сергей", "Сергеев", "Иванович", '11.11.1999', "8 гимназия", class_rooms[2], []),
            Student("Павел", "Алевсеев", "Сергеевич", '04.11.2003', "8 гимназия", class_rooms[2], []),
            Student("Инна", "Александрова", "Павловна", '03.11.1999', "8 гимназия", class_rooms[3], [parents[0], parents[1]]),
            Student("Мария", "Яковлева", "Алексеевна", '11.11.1999', "8 гимназия", class_rooms[3], [])]

print('1. Полный список всех классов школы')
for cl in class_rooms:
    print(cl.class_room)
print()
def get_list_students(class_room):
    return [st.get_surname_initials() for st in students if st.class_room == class_room]

print('2. Список всех учеников в', class_rooms[0].class_room)
print(get_list_students(class_rooms[0]))
print()
print('3. Список всех предметов ученика', students[0].get_surname_initials())
for subject in students[0].class_room.teachers_dict.keys():
    print(subject)
print()
print('4. ФИО родителей ученика', students[0].get_surname_initials())
for parent in students[0].parents:
    print(parent.get_full_name())
print()
print('5. Список учителей в классе', class_rooms[0].class_room)
for teacher in class_rooms[0].teachers_dict.values():
    print(teacher.get_full_name())
