# Задача №3615. Проценты Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме
# вклада. Вклад составляет X рублей Y копеек. Определите размер вклада через год.
#
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
#
# Входные данные
# Программа получает на вход целые числа P, X, Y.
#
# Выходные данные
# Программа должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается


def get_bet(p, x, y):
    all = int((x * 100 + y) * (100 + p) / 100)
    return all // 100, all % 100


def main():
    p = int(input())
    x = int(input())
    y = int(input())
    rub, kop = get_bet(p, x, y)
    print(rub, kop)


if __name__ == '__main__':
    main()
