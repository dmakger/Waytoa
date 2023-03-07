# Задача №112373. Диагонали
# Напишите программу, которая заполняет матрицу неотрицательными числами по диагоналям (см.
# пример). Значение элемента матрицы равно расстоянию от левого верхнего угла матрицы.
#
# Входные данные Во входной строке записаны через пробел размеры матрицы: количество строк N и количество столбцов M
# ( 1 ≤ N , M ≤ 100 ).
#
# Выходные данные
# Программа должна вывести полученную матрицу по строкам.


def get_matrix(size: int):
    return [[] for _ in range(size)]


def fill_snake_matrix(matrix: list, n: int, m: int):
    for i in range(n):
        for j in range(m):
            matrix[i].append(i + j)


def print_matrix(matrix: list):
    for line in matrix:
        print(*line, sep=' ')


def main():
    n, m = map(int, input().split())
    matrix = get_matrix(n)
    fill_snake_matrix(matrix, n, m)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
