# fruits: list[str, ...] = ['orange', 'strawberry', 'apple']
#
# nums: list[int, int] = [10, 20]
#
# chars: tuple[str, int] = ('a', 40)
#
# names: dict[str, str] = {
#     'name1': 'Jake',
#     'name2': 'Anna'
# }
#
#
# fruits, *y = fruits
# # x, y = fruits
#
# print('X', fruits)
# print('Y', y)
# print(fruits)

# ----------------------------------


# class Cat:
#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self.color = color
#
#     def __str__(self) -> str:
#         return self.name
#
#     def __repr__(self) -> str:
#         return f'class <{self.__class__.__name__}>: {self.name}'
#
#
# if __name__ == '__main__':
#     cat_1 = Cat('Рыжий', 'оранжевый')
#     print(cat_1)
#     print(repr(cat_1))


# def say_hello(foo):
#     foo('Привет, Мир!')
#
#
# say_hello(print)
#


line: str = input()

rows: int = 3
print((line + '\n') * rows, end='')
