# Задача №112175. Квадрат из звёздочек
# Напишите программу, которая строит "квадрат" из знаков '*' заданного размера. Используйте процедуру.
#
# Входные данные
# Входная строка содержит единственное натуральное число – длину стороны квадрата N .
#
# Выходные данные
# Программа должна вывести заполненный квадрат размером N × N , состоящий из знаков '*'


def main():
    n = int(input())
    print(*['*' * n] * n, sep='\n')


if __name__ == '__main__':
    main()
