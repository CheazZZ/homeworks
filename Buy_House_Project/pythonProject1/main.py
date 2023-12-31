class Human:
    default_name = None
    default_age = None

    def __init__(self, money, house, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        template: str = (f'\nThe name is {self.default_name}'
                         f'\nAge is {self.default_age}'
                         f'\nHouse is {self.__house}'
                         f'\nMoney = {self.__money}')
        print(template)

    @staticmethod
    def default_info(value) -> None:
        data: str = (f'\ndefault name is {value.default_name}'
                     f'\ndefault age is {value.default_age}')
        print(data)


human = Human(1_000_000,
              'big house',
              'Bob',
              12)
human.info()
# human.default_info(human)
