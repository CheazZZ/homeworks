class Phone:
    """Базовый класс."""

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        pass

    def call(self):
        pass

    def info(self):
        """
        Выводит короткую сводку по классу Phone.
        """
        print(f'Class name: {Phone.__name__}')
        print(f'If phone is ON: {self.is_on}')


class MobilePhone(Phone):
    """Унаследованный класс."""

    def __init__(self):
        super().__init__()
        self.battery = 0

    def info(self):
        """
        выводит короткую сводку по классу MobilePhone
        Обратите внимание, что названия у методов совпадают - оба метода называются info()
        Однако их содержимое различается
        """
        print(f'Class name: {MobilePhone.__name__}')
        print(f'If mobile phone is ON: {self.is_on}')
        print(f'Battery level: {self.battery}')


p_1 = Phone()
mp_1 = MobilePhone()

p_1.info()
print('----------------')
mp_1.info()
