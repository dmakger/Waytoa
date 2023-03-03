# Задача №306. Минимум 4 чисел
# Напишите функцию int min (int a, int b, int c, int d), находящую наименьшее из четырех данных чисел.
#
# Входные данные
# Вводится четыре числа.
#
# Выходные данные
# Необходимо вывести  наименьшее из 4-х данных чисел.

def minimum(*args):
    result = args[0]
    for i in range(1, len(args)):
        if result > args[i]:
            result = args[i]
    return result


def main():
    print(minimum(*map(int, input().split())))


if __name__ == '__main__':
    main()
