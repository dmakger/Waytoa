# Сегодня Патрик ждёт в гости своего друга Спанч Боба. Чтобы подготовиться к встрече,
# Патрику необходимо посетить два магазина, расположенных рядом с его домом.
# От дома до первого магазина ведёт дорожка длины d1 метров, а до второго магазина ведёт дорожка
# длины d2 метров. Также существует дорожка, непосредственно соединяющая два магазина друг с другом,
# длиной d3 метров. Помогите Патрику вычислить минимальное расстояние, которое ему потребуется пройти,
# чтобы посетить оба магазина и вернуться домой.
#
#
# Патрик всегда стартует дома. Он должен посетить оба магазина, перемещаясь только по имеющимся
# трём дорожкам, и вернуться назад домой. При этом его совершенно не смутит, если ему придётся посетить
# один и тот же магазин или пройти по одной и той же дорожке более одного раза. Единственная его
# задача — минимизировать суммарное пройденное расстояние.
#
# Входные данные
#
# d1 — длина дорожки, соединяющей дом Патрика и первый магазин;
# d2 — длина дорожки, соединяющей дом Патрика и второй магазин;
# d3 — длина дорожки, соединяющей два магазина.
# Выходные данные
# Выведите минимальное количество метров, которое придётся пройти Патрику, чтобы посетить оба магазина и вернуться домой.

def main():
    d1, d2, d3 = map(int, input().split())
    road1 = (d1 + d2) * 2
    road2 = d1 + d2 + d3
    road3 = (d1 + d3) * 2
    road4 = (d2 + d3) * 2
    print(min(road1, road2, road3, road4))


if __name__ == '__main__':
    main()