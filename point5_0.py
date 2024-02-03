class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __calc_distance(self, x1, y1, x2, y2) -> int | float:
        expr = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
        return round(expr ** 0.5, 2)

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def length(self, obj: 'Point') -> int | float:
        x1 = self.x
        y1 = self.y

        x2 = obj.x
        y2 = obj.y

        return self.__calc_distance(x1, y1, x2, y2)


class PatchedPoint(Point):

    def __init__(self,
                 x: int | tuple[int, int] = 0,
                 y: int = 0) -> None:
        if isinstance(x, tuple):
            x, y = x
        super().__init__(x=x, y=y)

    def __add__(self, other: int | tuple) -> tuple | int:
        return PatchedPoint(other)

    def __iadd__(self, other: int | tuple[int, int]) -> int | tuple:
        if isinstance(other, tuple):
            other_1, other_2 = other
            self.x += other_1
            self.y += other_2
        return self.x, self.y

    def __str__(self) -> str:
        return f"{self.x, self.y}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.x, self.y}"


first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
