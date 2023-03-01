# Задача №112180. Восьмеричный код (10 цифр)
# Напишите программу, которая переводит переданное ей неотрицательное целое число в 10-значный
# восьмеричный код, сохранив лидирующие нули. Используйте процедуру.
#
# Входные данные
# Входная строка содержит неотрицательное целое число N ( 0≤ N <8^10 ).
#
# Выходные данные
# Программа должна вывести 10-значный восьмеричный код переданного её числа, сохранив лидирующие нули.

# 65
# 8 1
# 1 0

def get_eight_form(ten: int, eight: str = ''):
    new_eight = str(ten % 8) + eight
    new_ten = ten // 8
    if new_ten > 7:
        return get_eight_form(new_ten, new_eight)
    return str(new_ten) + new_eight


def get_valid_form(data):
    data_str = str(data)
    return '0' * (10 - len(data_str)) + data_str


def main():
    print(get_valid_form(get_eight_form(int(input()))))


if __name__ == '__main__':
    main()
