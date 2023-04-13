# Задача №3612. Часы - 1
# С начала суток прошло H часов, M минут, S секунд (0≤H<12, 0≤M<60, 0≤S<60).
# По данным числам H, M, S определите угол (в градусах), на который повернулаcь
# часовая стрелка с начала суток и выведите его в виде действительного числа.
#
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
#
# Входные данные
# Вводятся три целых неотрицательных числа.
#
# Выходные данные
# Выведите ответ на задачу


def get_degree(h, m, s):
    degree_hour = 360 / 12
    degree_minutes = degree_hour / 60
    degree_seconds = degree_minutes / 60
    return (degree_hour * h + degree_minutes * m + degree_seconds * s) % 360


def main():
    h = int(input())
    m = int(input())
    s = int(input())
    print(get_degree(h, m, s))
    # print(get_degree(1, 2, 6))


if __name__ == '__main__':
    main()
