class Human:
    # 1. Укажите аннотации типа для всех идентификаторов.
    default_name = None
    default_age = None

    def __init__(self,
                 money,
                 house,
                 name=default_name,
                 age=default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        template: str = (f'\nThe name is {self.name}'
                         f'\nAge is {self.age}'
                         f'\nHouse is {self.__house}'
                         f'\nMoney = {self.__money}')
        print(template)

    @staticmethod
    def default_info() -> None:
        print(f'\nDefault name is - {Human.default_name}'
              f'\nDefault age is - {Human.default_age}')

    # 2. Метод реализован неправильно.
    # Согласно ТЗ, метод должен принимает
    # два аргумента: "объект дома и его цену.".
    """
    ТЗ:
    6. Реализуйте приватный метод make_deal(), который будет отвечать за 
    техническую реализацию покупки дома: уменьшать количество денег на 
    счету и присваивать ссылку на только что купленный дом. 
    В качестве аргументов данный метод принимает объект дома и его цену.
    """

    def __make_deal(self, cost) -> None:
        self.__money -= cost  # это правильно
        self.__house = self.name

    def earn_money(self, value) -> None:
        self.__money += value

    # 3. Нужно реализовать метод  buy_house().

    """
    ТЗ:
    8. Реализуйте метод buy_house(), который будет проверять, что у человека 
    достаточно денег для покупки, и совершать сделку. Если денег 
    слишком мало - нужно вывести предупреждение в консоль. Параметры метода: 
    ссылка на дом и размер скидки
    """


class House:
    # 4. Конструктор этого класса не должен иметь значение по умолчанию.
    def __init__(self,
                 area='30м2',
                 price=1_000_000):
        self._area = area
        self._price = price

    # 5. Нужно реализовать метод  buy_house().
    """
    ТЗ:
    3. Создайте метод final_price(), который принимает в качестве параметра 
    размер скидки и возвращает цену с учетом данной скидки.
    """

    def disc_percent(self, discount, full_price) -> float:
        full_price /= 100
        full_price *= discount
        return self._price - full_price


class SmallHouse(House):  # Здесь все хорошо!

    def __init__(self):
        super().__init__(area='40м2', price=500_000)


# -----------------------------

house_1 = House('100м2', 1_000_000)
discounted_price = house_1.disc_percent(10,
                                        1_000_000)

print(f'Final price of house is {discounted_price}')

small = SmallHouse()
small1 = small.disc_percent(50, 500_000)

print(f'Final price of small house is {small1}')
