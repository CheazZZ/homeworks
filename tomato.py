class Tomato:

    __STATES: dict = {
        'absent': 1,
        'blossom': 2,
        'green': 3,
        'red': 4,
    }

    def __init__(self, _index: str) -> None:
        self._state: dict = Tomato.__STATES['absent']
        self._index = _index

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


tomato = Tomato('absent')
print(tomato)
tomato.grow()
print(tomato)
