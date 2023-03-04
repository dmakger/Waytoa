# Задача №118. Обращение числа
# Напишите функцию int reverse(int n) (C/C++), function reverse (n:integer):integer (Pascal),
# которая переставляет цифры числа в обратном порядке .
#
# Входные данные
# Задано единственное число N
#
# Выходные данные
# Необходимо вывести цифры данного числа в обратном порядке.
from math import sqrt


def reverse(digit: int):
    return int(f'{digit}'[::-1])


def main():
    print(reverse(int(input())))


if __name__ == '__main__':
    main()
