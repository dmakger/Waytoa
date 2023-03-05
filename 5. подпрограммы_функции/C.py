# Задача №102. Проверить, является ли символ цифрой
# Напишите функцию boolean IsDigit(char c) (Java), function IsDigit(c:char):boolean (Pascal),
# bool IsDigit(unsigned char c) (C/C++), определяющую, является ли данный символ цифрой или нет.
#
# Естественно, программа должна считывать данные, вызывать эту функцию и выдавать ответ.
#
# Входные данные
# Задан единственный символ c.
#
# Выходные данные
# Необходимо вывести  строку yes, если символ является цифрой, и строку no в противном случае


def isDigit(digit):
    return 0 <= ord(digit) - ord('0') < 10


def main():
    print('yes' if isDigit(input()[0]) else 'no')


if __name__ == '__main__':
    main()
