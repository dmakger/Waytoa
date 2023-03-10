# Задача №114. Сумма цифр числа
# Дано натуральное число N. Напишите функцию int SumOfDigits (int n) (C/C++), function SumOfDigits
# (n:longint):integer (Pascal), вычисляющую сумму цифр числа N.
#
# Входные данные
# Задано единственное число N
#
# Выходные данные
# Необходимо вывести  сумму цифр числа N.
from math import sqrt


def SumOfDigits(digit: int):
    return sum(int(x) for x in str(digit))


def main():
    print(SumOfDigits(int(input())))


if __name__ == '__main__':
    main()
