# Задача №116. Минимальная и максимальная цифры
# Дано натуральное число N. Напишите функцию int MinDigit (int n) (C/C++), function MinDigit (n:longint):integer
# (Pascal) и int MaxDigit (int n) (C/C++), function MaxDigit (n:longint):integer (Pascal), определяющую
# наименьшую и наибольшую цифры данного числа.
#
# Входные данные
# Задано единственное число N
#
# Выходные данные
# Необходимо вывести наименьшую и наибольшую цифры данного числа через пробел


def MinDigit(digit: int):
    return min(x for x in str(digit))


def MaxDigit(digit: int):
    return max(x for x in str(digit))


def main():
    digit = int(input())
    print(MinDigit(digit), MaxDigit(digit))


if __name__ == '__main__':
    main()
