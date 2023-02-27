# Задача №111330. Обращение всего файла
# Выведите в обратном порядке содержимое всего файла полностью.
# Для этого считайте файл целиком при помощи метода read().

def has_symbol(filename, symbol):
    with open(filename, 'r') as fin:

        for line in fin:
            if '@' in line:
                fin.close()
                return 'YES'
        return 'NO'


def main():
    print(has_symbol('input.txt', '@'))


if __name__ == '__main__':
    main()
