# Задача №3614. Часы - 3 С начала суток часовая стрелка повернулась на угол в α градусов. Определите сколько полных
# часов, минут и секунд прошло с начала суток, то есть решите задачу, обратную задаче E. Запишите ответ в три
# переменные и выведите их на экран.
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

    h = int(degree // degree_hour)
    m = int(degree % degree_hour // degree_minutes)
    s = int(degree % degree_minutes // degree_seconds)

    return h, m, s


def main():
    degree = float(input())
    h, m, s = get_degree(degree)
    print(h, m, s)


if __name__ == '__main__':
    main()
