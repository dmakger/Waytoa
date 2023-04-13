# Задача №3611. Площадь треугольника
# Даны длины сторон треугольника. Вычислите площадь треугольника.
#
# Входные данные
# Вводятся три положительных числа.
#
# Выходные данные
# Выведите ответ на задачу.
# from math import sqrt


def round_5(digit):
    part = int(digit * 10) % 10
    digit_int = int(digit)
    if part > 4:
        return digit_int + 1
    return digit_int


def area_triangle(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s
    # degree = 10**6
    # d = round_5(s * degree)
    # return d / degree
    # return int(s * degree) / degree


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(area_triangle(a, b, c))


if __name__ == '__main__':
    main()
