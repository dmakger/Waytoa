# Задача №3613. Часы - 2 С начала суток часовая стрелка повернулась на угол в α градусов. Определите на какой угол
# повернулась минутная стрелка с начала последнего часа. Входные и выходные данные — действительные числа.
#
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
#
# Входные данные
# Вводится неотрицательное действительное число.
#
# Выходные данные
# Выведите ответ на задачу.


def get_degree(degree):
    degree_hour = 360 / 12
    degree_minutes = degree_hour / 60
    degree_seconds = degree_minutes / 60

    hours = degree % degree_hour
    print(hours % degree_minutes % degree_seconds)
    minutes = hours // degree_minutes
    return minutes * (360 / 60)


def main():
    # degree = int(input())
    # print(get_degree(degree))
    print(get_degree(201))


if __name__ == '__main__':
    main()
