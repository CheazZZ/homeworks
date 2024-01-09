from string import ascii_uppercase


class Alphabet:

    def __init__(self, lang: str, letters: list | str) -> None:
        self.lang = lang
        self.letters = letters

    def print(self) -> None:
        print(self.letters)

    def letters_num(self) -> int | float:
        return len(self.letters)


class EngAlphabet(Alphabet):

    __letters_num: int | float = 0

    def __init__(self,
                 en_lang='En',
                 en_letters=ascii_uppercase) -> None:
        self.lang = en_lang
        self.letters = en_letters
        super().__init__(lang=en_lang, letters=en_letters)

    def is_en_letter(self, check_num: str) -> None:
        if check_num.upper() in self.letters:
            print(f"{check_num} is an english letter")
        else:
            print("Wrong letter!")

    def letters_num(self) -> int | float:
        super().letters_num()
        return EngAlphabet.__letters_num

    @staticmethod
    def example() -> str:
        return 'Example for class: EngAlphabet'
