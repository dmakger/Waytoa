# Задача №3624. Экспонента
# По данному целому числу n и действительному числу x вычислите сумму 1+x1!+x22!+x33!+...+xnn!
#
# Операцией возведения в степень пользоваться нельзя. Алгоритм должен иметь сложность O(n).
#
# Входные данные
# Вводятся натуральное число n и действительное число x.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примечание
# Этот ряд сходится к ex при росте n.

def e(n: int, x: float):
    r = 1
    numerator = 1
    denominator = 1
    for i in range(1, n + 1):
        numerator *= x
        denominator *= i
        r += numerator/denominator
    return r


def main():
    print(e(int(input()), float(input())))


if __name__ == '__main__':
    main()
