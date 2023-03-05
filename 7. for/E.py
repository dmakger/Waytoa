# Задача №317. Число сочетаний
# По данным натуральным n и k вычислите значение Ckn=n!k!(n−k)! (число сочетаний из n элементов по k).
#
# Входные данные
# Вводятся 2 числа - n и k (n,k≤30).
#
# Выходные данные
# Необходимо вывести  значение Ckn.

def factorial(n: int):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def count_combinations(n: int, k: int):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def main():
    print(count_combinations(int(input()), int(input())))


if __name__ == '__main__':
    main()
