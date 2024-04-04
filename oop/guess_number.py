from random import randint

# Про randint можете почитать здесь
# https://docs-python.ru/standart-library/modul-random-python/sluchajnye-tselye-chisla-modulja-random/

# Случайное число в диапазоне от 1 до 100 включительно
num = randint(1, 100)

attempts = 0
user_num = int(input('Введите число от 1 до 100: '))
while True:
    if user_num == num:
        print(f'Поздравляем! Вы угадали число {num} за {attempts} попыток')
        break

    if user_num < num:
        print('Ваше число меньше загаданного..')
    elif user_num > num:
        print('Ваше число больше загаданного..')

    # TODO: Info: Ниже стоящие две строки кода вынести после блоков if elif,
    #  если пользователь угадал число срабатывает break
    user_num = int(input('Введите число от 1 до 100: '))
    attempts += 1

# TODO: 1. В целом задача реализована хорошо, дублирование кода убрано.

# TODO: 2. Также можно доработать задачу, иначе у пользователя будет бесконечное
#  количество попыток угадать число.
