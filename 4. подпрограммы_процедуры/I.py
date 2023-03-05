# Задача №112179. Римская система
# Напишите программу, которая выводит запись переданного ей числа в римской системе счисления. Используйте процедуру.
#
# Входные данные
# Входная строка содержит натуральное число N ( 1 ≤ N ≤ 3999 ).
#
# Выходные данные
# Программа должна вывести запись числа N в римской системе счисления.

def in_roman_system(n: int):
    DATA = [
        ['I', 'V'],
        ['X', 'L'],
        ['C', 'D'],
        ['M', ''],
    ]

    digit_reverse_str = str(n)[::-1]
    result = ''
    for i in range(len(digit_reverse_str)):
        cur = int(digit_reverse_str[i])
        if cur < 4:
            result = cur * DATA[i][0] + result
        elif cur == 4:
            result = DATA[i][0] + DATA[i][1] + result
        elif cur < 9:
            result = DATA[i][1] + DATA[i][0] * (cur - 5) + result
        elif cur == 9:
            result = DATA[i][0] + DATA[i+1][0] + result
    return result


def main():
    print(in_roman_system(int(input())))


if __name__ == '__main__':
    main()
