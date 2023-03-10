# Задача №111. Капитан Флинт
# Капитан Флинт зарыл клад на Острове сокровищ. Он оставил описание, как найти клад.
# Описание состоит из строк вида: "North 5", где  слово – одно из "North", "South", "East", "West",
# – задает направление движения, а  число – количество шагов, которое необходимо пройти в этом направлении.
#
# Напишите программу, которая по описанию пути к кладу определяет точные координаты клада, считая, что начало
# координат находится в начале пути, ось OX направлена на восток, ось OY – на север.
#
# Входные данные
# На вход подается последовательность строк указанного формата. Гарантируется, что числа не превосходят 108.
#
# Выходные данные
# Необходимо вывести  координаты клада – два целых числа через пробел.
# Гарантируется, что эти числа не превосходят  108

def main():
    cardinal = {
        'North': {'pos': 'y', 'digit': 1},
        'South': {'pos': 'y', 'digit': -1},
        'East': {'pos': 'x', 'digit': 1},
        'West': {'pos': 'x', 'digit': -1},
    }

    with open('input.txt', 'r') as fin:
        result = {'x': 0, 'y': 0}
        for line in fin:
            cardinal_name, distance = line.split()
            result[cardinal[cardinal_name]['pos']] += int(distance) * cardinal[cardinal_name]['digit']
        print(*result.values())


if __name__ == '__main__':
    main()
