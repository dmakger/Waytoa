# Задача №338. Переверни число
# Входные данные
# Вводится натуральное число x
#
# Выходные данные
# Выведите число, состоящее из цифр данного числа x в обратном порядке. Ведущие нули выводить не нужно


def reverse_digit(digit: int):
    r = str(digit)[::-1]
    for i in range(len(r)):
        if r[i] != '0':
            return r[i:]
    return ''


def main():
    print(reverse_digit(int(input())))


if __name__ == '__main__':
    main()
