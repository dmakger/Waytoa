# Задача №112177. Цифры числа - 2
# Напишите программу, которая выводит в столбик цифры введённого числа, начиная с первой. Используйте процедуру.
#
# Входные данные
# Входная строка содержит неотрицательное число N .
#
# Выходные данные
# Программа должна вывести в столбик все цифры введённого числа, начиная с первой


def main():
    print(*input(), sep='\n')


if __name__ == '__main__':
    main()
