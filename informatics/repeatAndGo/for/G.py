# Задача №3553. Потерянная карточка
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее,
# зная номера оставшихся карточек.
#
# Входные данные
# Дано число N, далее N-1 номер оставшихся карточек (различные числа от 1 до N).
#
# Выходные данные
# Программа должна вывести номер потерянной карточки.
#
# Примечание
# Для самых умных – массивами и аналогичными структурами данных пользоваться нельзя.
import math


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    count = 0
    for i in range(1001):
        if i != e:
            if a * i * i * i + b * i * i + c * i + d == 0:
                count += 1
    print(count)


if __name__ == '__main__':
    main()