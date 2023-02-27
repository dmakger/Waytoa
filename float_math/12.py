# Задача №3618. Квадратное уравнение - 1 Даны действительные коэффициенты a, b, c, при этом a≠0. Решите квадратное
# уравнение ax2+bx+c=0 и выведите все его корни.
#
# Входные данные
# Вводятся три действительных числа.
#
# Выходные данные Если уравнение имеет два корня, выведите два корня в порядке возрастания, если один корень —
# выведите одно число, если нет корней — не выводите ничего
from decimal import Decimal
from math import sqrt


def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    first = (-b + sqrt(d)) / 2 * a
    if d == 0:
        return [first]

    return (
        first,
        (-b - sqrt(d)) / 2 * a,
    )


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    result = discriminant(a, b, c)
    # result = discriminant(1, -4, -21)
    # result = discriminant(1, -1, -2)
    if result is not None:
        for el in sorted(result):
            print(int(el), end=' ')


if __name__ == '__main__':
    main()
