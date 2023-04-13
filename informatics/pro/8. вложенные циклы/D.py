# Задача №111366. Побочная диагональ
# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.

def get_matrix(size: int):
    return [[] for _ in range(size)]


def fill_side_diagonal(matrix: list, size: int):
    for i in range(size):
        for j in range(size):
            digit = size - i - 1
            if j < digit:
                matrix[i].append(0)
            elif j > digit:
                matrix[i].append(2)
            else:
                matrix[i].append(1)


def print_matrix(matrix: list):
    for line in matrix:
        print(*line, sep=' ')


def main():
    size = int(input())
    matrix = get_matrix(size)
    fill_side_diagonal(matrix, size)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
