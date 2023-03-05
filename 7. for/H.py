# Задача №3625. Косинус
# По данному целому числу n и действительному числу x вычислите сумму 1−x22!+x44!−x66!+...+(−1)nx2n(2n)!
#
# Операцией возведения в степень и функцией factorial пользоваться нельзя. Алгоритм должен иметь сложность O(n).
#
# Входные данные
# Вводится натуральное число n и действительное число x.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примечание
# Этот ряд сходится к cosx при росте n (углы измеряются в радианах).
from decimal import Decimal


def cos(n: int, x: Decimal):
    r = 1
    numerator = 1
    denominator = 1
    for i in range(1, n + 1):
        numerator *= x * x
        denominator *= i*2 * (i*2-1)
        r -= Decimal(numerator/denominator) * (-1 + (i % 2 * 2))
    return r


def main():
    print(cos(int(input()), Decimal(input())))


if __name__ == '__main__':
    main()
