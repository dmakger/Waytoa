# Задача №112372. В шахматном порядке
# Заполнить двоичную матрицу (состоящую только из нулей и единиц) в шахматном
# порядке. В левом верхнем углу должен быть нулевой элемент.
#
# Входные данные Во входной строке записаны через пробел размеры матрицы: количество строк N и количество столбцов M
# ( 1 ≤ N , M ≤ 100 ).
#
# Выходные данные
# Программа должна вывести двоичную матрицу по строкам.


def get_matrix(size: int):
    return [[] for _ in range(size)]


def fill_chess_board(matrix: list, n: int, m: int):
    brush = [0, 1]
    count_brush = len(brush)

    for i in range(n):
        for j in range(m):
            matrix[i].append(brush[(j + i) % count_brush])


def print_matrix(matrix: list):
    for line in matrix:
        print(*line, sep=' ')


def main():
    n, m = map(int, input().split())
    matrix = get_matrix(n)
    fill_chess_board(matrix, n, m)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
