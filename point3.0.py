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

    def __init__(self, *args) -> None:
        super().__init__(x=0, y=0)
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args


point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
