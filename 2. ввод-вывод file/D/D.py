# Задача №111329. Построчное обращение
# Выведите все строки данного файла в обратном порядке. Для этого считайте
# список всех строк при помощи метода readlines().
#
# Последняя строка входного файла обязательно заканчивается символом '\n'.

def main():
    with open('input.txt', 'r') as fin:
        print(''.join(fin.readlines()[::-1]), end='')


if __name__ == '__main__':
    main()
