class Tomato:
    # 1. Лучше следовать ТЗ, у помидора стадии указаны на русском:
    """
    Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
    """

    # Тогда лучше сделать так:
    # __STATES: dict[int, str] = {
    #     1: 'Отсутствует',
    #     2: 'Цветение',
    #     3: 'Зеленый',
    #     4: 'Красный'
    # }
    # Объяснение: Когда каждая стадия, указывается под определенным
    # номером (числом), то легче будет отслеживать стадии у помидоров
    # и обратать, для этого Вам понадобится создать дополнительный
    # динамический атрибут (свойство) в инициализаторе

    __STATES: dict = {
        'absent': 1,
        'blossom': 2,
        'green': 3,
        'red': 4,
    }

    # 2. Необязательно сделать параметр с нижнем подчеркиванием.
    # Сделайте, чтобы параметр был index, а атрибут все верно сделали,
    # соблюдаем принцип инкапсуляции.
    def __init__(self, _index: str) -> None:
        self._state: dict = Tomato.__STATES['absent']
        self._index = _index
        self.__current_state = 1  # 3. Добавил атрибут, который говорил выше,
        # по умолчанию у всех помидоров стадия под номером 1. С таким
        # подходом у Вас исчезнут условные блоки, дальше попробуйте
        # реализовать задачу по такому подходу.

    def __get_index(self) -> int:
        return Tomato.__STATES[self._index]

    def __set_state(self) -> None:
        if self.__get_index() < 2:
            self._index = Tomato.__STATES['blossom']
        elif self.__get_index() < 3:
            self._index = Tomato.__STATES['green']
        elif self.__get_index() < 4:
            self._index = Tomato.__STATES['red']

    def grow(self) -> None:
        self.__set_state()

    def __str__(self) -> str:
        return f"{self._index, self._state}"


# 4. Задача реализована не полностью, также нужно реализовать следующие классы:
# - TomatoBush
# - Gardener
# - И тесты к коду.

tomato = Tomato('absent')
print(tomato)
tomato.grow()
print(tomato)
