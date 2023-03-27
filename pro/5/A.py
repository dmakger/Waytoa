# Он заметил, что два кролика прыгали навстречу друг другу. Позиции двух кроликов можно задать целочисленными
# координатами на горизонтальной прямой. Более высокий кролик изначально находится в точке с координатой x, а
# более низкий — в точке с координатой y (x<y). Каждую секунду, каждый кролик прыгает на другую позицию. Более
# высокий кролик прыгает в положительном направлении на a, а более низкий прыгает в отрицательном направлении на b.
#
#
# Например, если x=0, y=10, a=2, и b=3. После 1-й секунды, кролики будут в точках 2 и 7. После 2-й секунды,
# оба кролика будет в точке 4.
#
# Гильдонг задумался: Будут ли когда-то два кролика в одной точке в один момент времени? Если будут,
# то через какое время это произойдет? Помогите ему найти такую секунду, после которой оба кролика будут в одной точке.
#
# Входные данные
# Каждый тест состоит из одного или более наборов входных данных. В первой строке записано количество
# наборов входных данных t (1≤t≤1000).
#
# Каждый набор входных данных состоит из ровно одной строки. Строка состоит из четырех целых чисел
# x, y, a, b (0≤x<y≤109, 1≤a,b≤109) — текущая позиция более высокого кролика, текущая позиция более низкого
# кролика, расстояние прыжка более высокого прыжка, расстояние прыжка более низкого кролика, соответственно.
#
# Выходные данные
# Для каждого набора входных данных, выведите одно целое число — количество секунд, через которое два кролика
# окажутся в одной точке.
#
# Если два кролика никогда не окажутся в одной точке одновременно, выведите −1.

def get_result(x, y, a, b):
    distance = y - x
    step = a + b
    if distance % step:
        return -1
    return distance // step


def main():
    for _ in range(int(input())):
        print(get_result(*map(int, input().split())))




if __name__ == '__main__':
    main()
