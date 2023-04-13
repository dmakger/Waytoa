# Задача №111378. Заполнение змейкой
# По данным числам n и m заполните двумерный массив размером n×m числами от 1 до n×m “змейкой”, как показано в примере.
#
# Входные данные
# Вводятся два числа n и m
#
# Выходные данные
# Выведите полученный массив, отводя на вывод каждого элемента ровно 4 символа.

def get_snake_matrix(n: int, m: int):
    matrix = []
    for i in range(n):
        mas = [x for x in range(m * i + 1, m * i + m + 1)]
        if i % 2:
            mas = mas[::-1]
        matrix.append(mas)
    return matrix


def print_matrix(matrix: list):
    count_space = 4
    for line in matrix:
        for el in line:
            print(f"{' ' * (count_space - len(str(el)))}{el}", end='')
        print()


def main():
    print_matrix(get_snake_matrix(*map(int, input().split())))


if __name__ == '__main__':
    main()
