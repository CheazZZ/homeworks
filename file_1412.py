# x = 10
#
# c = x * 2
#
# print('Привет, Мир!')
#
# for i in range(10):
#     print(i, end=' ')
#
# print(4 * 5)
#
#
# a = int(input())
# b = int(input())
#
# # классика
# stol = a
# a = b
# b = stol
#
# print(a, b)
#
# # Python
# a, b = (b, a)

# ----------------

# Функциональное програмированине


# def hello_world():
#     print('Привет, Мир!')
#
#
# def two_sum(x, y):
#     return x + y
#
#
# def run():
#     print(two_sum(10, 30))
#     hello_world()
#
#
# run()
#
# # Объектно-ориентированное программирование
# line = 'World'
# line.upper()
#
#
# # None - ничего --> null


# class Human:
#     # атрибут класса, свойство
#     # NAME = None
#     # DATE_OF_BIRTH = None
#     # SEX = None
#
#     def __init__(this, name, date_of_birth, sex):
#         this.name = name
#         this.date_of_birth = date_of_birth
#         this.sex = sex
#
#     # методы - поведение объекта
#     def say(self):
#         print('Я говорю!')
#
#     def think(self):
#         print('Я думаю!')
#
#     def walk(self):
#         print('Я гуляю!')
#
#     def info(this):
#         print(f'Меня зовут {this.name}! '
#               f'Дата рождения: {this.date_of_birth}. '
#               f'Пол: {this.sex}')
#
#         # print(f'Меня зовут {self.NAME}')
#
#
# petya = Human('Петя', '01.01.1970', 'М')  # ул.1-ая д.10
# # petya.NAME = 'Петя'
# petya.info()

# vasya = Human('Вася', '08.08.1990', 'М')  # ул.4-ая д.43
# vasya.info()


class Animal:
    def __init__(self, name, age, sex, date_of_birth):
        self.name = name
        self.age = age
        self.sex = sex
        self.date_of_birth = date_of_birth

    def run(self):
        print("I can run faster, than you!")

    def scratch(self):
        print('scratching')

    def voice(self):
        print("there is some voice of animal here")

    def jump(self):
        return 'Jump!'

    def info(self):
        print(f"Моя кличка: {self.name}! "
              f"Мой пол: {self.sex} "
              f"Мне {self.age} лет. " 
              f"Я родился {self.date_of_birth} гг.")


barsik = Animal('Барсик', 10, 'мужской', "01.01.1998")
barsik.info()

# vasya = Animal('vasya', 10, 'male', 1998)
# print(vasya.jump())
# vasya_jump = vasya.jump()
# print(vasya_jump)
#
# some_word = 'Vasya'
# concatenate = some_word + ', ' + vasya_jump
# print(concatenate)


# class Cat(Animal):
#
#     def iscat(self):
#         return True
#
#     def not_dog(self):
#         if not cat:
#             print("It's another class!")



# cat = Cat('Tom', 11, 'male', 1997)
# print(cat.iscat())
# print(cat.jump())
# print(cat.sex)
# cat1 = Cat('Снежок', 13, )