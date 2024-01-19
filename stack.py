class Stack:

    def __init__(self) -> None:
        self.__stack = []

    def is_empty(self) -> bool:
        return not self.__stack

    def pop(self, value) -> int | float:
        return self.__stack.pop(value)

    def push(self, item) -> None:
        self.__stack.append(item)

    def show(self) -> None:
        print(self.__stack)


stack = Stack()


for n in range(10):
    stack.push(n)

stack.show()

while not stack.is_empty():
    print(stack.pop(-1), end=" ")

print()
stack.show()
