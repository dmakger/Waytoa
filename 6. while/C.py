# Задача №115. Количество нулей
# Дано натуральное число N. Напишите функцию int NumberOfZeroes(int n) (C/C++/Java),
# function NumberOfZeroes(n: longint): integer (Pascal), определяющую количество нулей среди всех цифр числа N.
#
# Входные данные
# Задано единственное число N
#
# Выходные данные
# Необходимо вывести количество нулей среди всех цифр числа N.

def NumberOfZeroes(digit: int):
    return str(digit).count('0')


def main():
    print(NumberOfZeroes(int(input())))


if __name__ == '__main__':
    main()
