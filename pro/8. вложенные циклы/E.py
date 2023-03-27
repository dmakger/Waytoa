# Задача №111365. Диагонали параллельные главной
# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали
# должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух
# диагоналях числа 2, и т.д.

def get_matrix(size: int):
    return [[] for _ in range(size)]


def fill_matrix(matrix: list, size: int):
    for i in range(size):
        for j in range(size):
            matrix[i].append(abs(j - i))


def print_matrix(matrix: list):
    for line in matrix:
        print(*line, sep=' ')


def main():
    size = int(input())
    matrix = get_matrix(size)
    fill_matrix(matrix, size)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
