# Задача №112376. Змейка-2
# Напишите программу, которая заполняет матрицу из N строк и M столбцов натуральными числами
# змейкой, как показано в примере.
#
# Входные данные
# Входная строка содержит числа N и M ( 1 ≤ N , M ≤ 100 ), разделённые пробелом.
#
# Выходные данные
# Программа должна вывести матрицу, заполненную заданным способом.


def get_matrix(size: int):
    return [[] for _ in range(size)]


def fill_snake_matrix(matrix: list, n: int, m: int):
    for i in range(m):
        index = 0
        sign = -1
        if i % 2:
            index = n - 1
            sign = 1
        for j in range(n):
            matrix[index - j * sign].append(i * n + j + 1)


def get_count_space(rows: int, cols: int):
    r = len(str(rows * cols)) + 1
    if r < 4:
        return 4
    return r


def print_matrix(matrix: list, count_space: int):
    for line in matrix:
        for el in line:
            print(f"{' ' * (count_space - len(str(el)))}{el}", end='')
        print()


def main():
    n, m = map(int, input().split())
    matrix = get_matrix(n)
    fill_snake_matrix(matrix, n, m)
    print_matrix(matrix, get_count_space(n, m))


if __name__ == '__main__':
    main()
