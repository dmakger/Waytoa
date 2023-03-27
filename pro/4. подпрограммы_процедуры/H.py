# Задача №112181. Шестнадцатеричный код (4 цифры)
# Напишите программу, которая переводит переданное ей неотрицательное целое число в четырёхзначный шестнадцатеричный код, сохранив лидирующие нули. Используйте процедуру.
#
# Входные данные
# Входная строка содержит неотрицательное целое число N ( 0 ≤ N < 16 4 ).
#
# Выходные данные
# Программа должна вывести четырёхзначный шестнадцатеричный код переданного её числа, сохранив лидирующие нули. Используйте прописные латинские буквы.

# 255
# 8 1
# 1 0

SIXTEEN = '0123456789ABCDEF'


def get_sixteen_form(ten: int, sixteen: str = ''):
    new_sixteen = str(SIXTEEN[ten % 16]) + sixteen
    new_ten = ten // 16
    if new_ten > 15:
        return get_sixteen_form(new_ten, new_sixteen)
    return SIXTEEN[new_ten] + new_sixteen


def get_valid_form(data):
    data_str = str(data)
    return '0' * (4 - len(data_str)) + data_str


def main():
    print(get_valid_form(get_sixteen_form(int(input()))))


if __name__ == '__main__':
    main()
