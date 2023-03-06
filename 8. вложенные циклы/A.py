# Задача №111364. Шахматная доска
# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*"
# в шахматном порядке. В левом верхнем углу должна стоять точка.


def chess_board(n: int, m: int):
    brush = ['.', '*']
    count_brush = len(brush)

    for i in range(n):
        for j in range(m):
            print(brush[(j + i) % count_brush ], end=' ')
        print()


def main():
    chess_board(*map(int, input().split()))


if __name__ == '__main__':
    main()
