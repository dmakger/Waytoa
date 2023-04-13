# Задача №307. Степень
# Напишите функцию double power (double a, int n) (C/C++), вычисляющую значение an.
# Входные данные
# Вводится 2 числа - a (вещественное) и n (целое неотрицательное).
#
# Выходные данные
# Необходимо вывести  значение an.


def power(digit, n):
    return digit ** n


def main():
    print(power(*map(float, input().split())))


if __name__ == '__main__':
    main()
