class Human:
    default_name: str | None = None
    default_age: int | None = None

    def __init__(self,
                 name: str = default_name,
                 age: int = default_age) -> None:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self) -> None:
        print(f'\nThe name is {self.name}'
              f'\nAge is {self.age}'
              f'\nHouse is {self.__house}'
              f'\nMoney = {self.__money}')

    @staticmethod
    def default_info() -> None:
        print(f'\nDefault name is - {Human.default_name}'
              f'\nDefault age is - {Human.default_age}')

    def __make_deal(self, obj: 'House', cost: int | float) -> None:
        self.__money -= cost
        self.__house = obj

    def earn_money(self, value: int | float) -> None:
        self.__money += value

    def buy_house(self, obj: 'House', disc: float) -> None:
        house_price: float = obj.final_price(disc)

        if self.__money < house_price:
            raise ValueError('Недостаточно денег')

        self.__make_deal(obj=obj, cost=house_price)

    def __str__(self) -> str:
        return (f'\nThe name is {self.name}'
                f'\nAge is {self.age}'
                f'\nHouse is {self.__house}'
                f'\nMoney = {self.__money}')


class House:
    def __init__(self,
                 area: str,
                 price: int | float) -> None:
        self._area = area
        self._price = price

    def final_price(self, discount: float) -> float:
        return self._price - (self._price * (discount / 100))


class SmallHouse(House):
    def __init__(self, small_area='40м2', small_price=500):
        self.area = small_area
        self.price = small_area
        super().__init__(area=small_area, price=small_price)

    def __str__(self):
        return f'Площадь: {self.area} Цена: {self.price}'


Human.default_info()

h_1 = Human('Алекс', 18)
# h_1.info()

print(h_1)

small_1 = SmallHouse()
h_1.earn_money(1000)
h_1.buy_house(small_1, 50)
# h_1.info()
print(h_1)
# -----------------------------
#
# house_1 = House('100м2', 1_000_000)
# discounted_price = house_1.disc_percent(10,
#                                         1_000_000)
#
# print(f'Final price of house is {discounted_price}')
#
# small = SmallHouse()
# small1 = small.disc_percent(50, 500_000)
#
# print(f'Final price of small house is {small1}')
