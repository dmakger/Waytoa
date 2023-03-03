# Задача №112190. Судейство
# На соревнованиях выступление спортсмена оценивают 5 экспертов, каждый из них выставляет оценку в баллах
# (целое число). Для получения итоговой оценки лучшая и худшая из оценок экспертов отбрасываются,
# а для оставшихся трёх находится среднее арифметическое. Напишите программу, которая принимает 5 оценок
# экспертов и возвращает итоговую оценку спортсмена. Используйте функцию для вычисления итоговой оценки.
#
# Входные данные
# Входная строка содержит 5 неотрицательных целых чисел, разделённых пробелами.
#
# Выходные данные
# Программа должна вывести в первой строке отброшенные оценки экспертов (минимальную, затем максимальную),
# разделив их пробелами. Во второй строке выводится одно вещественное число: итоговая оценка с двумя знаками
# в дробной части.

def judging(*args):
    minn = args[0]
    maxx = args[0]
    for v in args:
        if minn > v:
            minn = v
        elif maxx < v:
            maxx = v

    summ = 0
    count = 0
    for v in args:
        if minn != v != maxx:
            count += 1
            summ += v
    result = f"{summ / count}"
    parts = result.split('.')
    if len(parts[1]) < 2:
        return minn, maxx, result + '0'
    return minn, maxx, parts[0] + '.' + parts[1][:2]


# def judging(*args):
#     minn, maxx = min(args), max(args)
#     result = f"{sum(args) - minn - maxx / (len(args) - 2)}"
#     parts = result.split('.')
#     if len(parts[1]) < 2:
#         return minn, maxx, result + '0'
#     return minn, maxx, parts[0] + '.' + parts[1][:2]


def main():
    minn, maxx, result = judging(*map(int, input().split()))
    print(minn, maxx)
    print(result)


if __name__ == '__main__':
    main()
