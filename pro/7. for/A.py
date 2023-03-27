# Задача №3620. Сумма ряда
# По данному числу n вычислите сумму 1+122+132+...+1n2.
#
# Входные данные
# Вводится целое положительное число.
#
# Выходные данные
# Выведите ответ на задачу.


def sum_row(digit: int):
    summ = 1
    for i in range(2, digit + 1):
        summ += (1 / i**2)
    return summ


def main():
    print(sum_row(int(input())))


if __name__ == '__main__':
    main()
