# Задача №117. Двоичная запись
# Дано натуральное число N. Выведите его представление в двоичном виде в обратном порядке.
#
# Входные данные
# Задано единственное число N
#
# Выходные данные
# Необходимо вывести требуемое представление числа N.


def in_system_two(ten: int, two: str = ''):
    two = str(ten % 2) + two
    part = ten // 2
    if part != 0:
        return in_system_two(part, two)
    return two


def main():
    print(in_system_two(int(input()))[::-1])


if __name__ == '__main__':
    main()
