import abc


class Animal(abc.ABC):
    """Абстрактный класс."""

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def scratch(self):
        pass

    @abc.abstractmethod
    def voice(self):
        pass

    @abc.abstractmethod
    def jump(self):
        pass


class AnimalBase(Animal):
    """Базовый класс для животных."""

    def __init__(self, name, sex, date_of_birth):
        self.name = name
        self.sex = sex
        self.date_of_birth = date_of_birth

    def run(self):
        print('I can run faster, than you!')

    def scratch(self):
        print('Scratching')

    def voice(self):
        print('There is some voice of animal here')

    def jump(self):
        print('Jump!')

    def __get_was_born(self):
        if self.sex == 'мужской':
            return 'родился'
        elif self.sex == 'женский':
            return 'родилась'

    def get_info(self):
        template: str = ('\nПривет!'
                         f'\nМоя кличка: {self.name}!'
                         f'\nМой пол: {self.sex}'
                         f'\nЯ {self.__get_was_born()} '
                         f'{self.date_of_birth}г.')
        print(template)
        # return template


class Cat(AnimalBase):
    def __init__(self, name, sex, date_of_birth):
        super().__init__(name, sex, date_of_birth)


class Dog(AnimalBase):
    def __init__(self, name, sex, date_of_birth):
        super().__init__(name, sex, date_of_birth)


class Lion(AnimalBase):
    def __init__(self, name, sex, date_of_birth):
        super().__init__(name, sex, date_of_birth)


# ----------------------------------------

barsik = Cat('Барсик', 'мужской', "01.01.1998")
barsik.get_info()

murzik = Cat('Мурзик', 'мужской', '02.03.1997')
# murzik.get_info()

animal_snezhok = Cat('Снежок', 'мужской', '03.05.2001')
# animal_snezhok.get_info()

animal_snezhana = Cat('Снежана', 'женский', '04.06.2002')
animal_snezhana.get_info()

# ----------------------------------------

# Dog
alabay = Dog('Алабай', 'мужской', '01.01.1970')
doberman = Dog('Доберман', 'мужской', '01.01.1970')
ejevicka = Dog('Ежевичка', 'женский', '01.01.1970')

alabay.get_info()
ejevicka.get_info()


# Нет необходимости получать параметр age: это можно легко рассчитать,
# зная год рождения. Текущий_год — Год_рождения = возраст
