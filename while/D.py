# Задача №336. Цифра в числе
# Входные данные
# Вводятся 2 числа: x и d.
#
# Выходные данные
# Подсчитайте и выведите одно число - сколько раз встречается в записи натурального числа x цифра d.


def count_digit_in_digit(x: int, d: int):
    return str(x).count(str(d))


def main():
    # print(count_digit_in_digit(*map(int, input().split()[:2])))
    print(count_digit_in_digit(int(input()), int(input())))


if __name__ == '__main__':
    main()
