# Задача №112176. Цифры числа - 1
# Напишите программу, которая выводит в столбик цифры введённого числа, начиная с последней. Используйте процедуру.
#
# Входные данные
# Входная строка содержит неотрицательное число N .
#
# Выходные данные
# Программа должна вывести в столбик все цифры введённого числа в обратном порядке, начиная с последней


def main():
    print(*(input()[::-1]), sep='\n')


if __name__ == '__main__':
    main()
