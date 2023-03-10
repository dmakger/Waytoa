# Задача №111162. Такси
# После затянувшегося совещания директор фирмы решил заказать такси,чтобы развезти сотрудников по домам. Он заказал N машин —ровно столько, сколь у него сотрудников.Однако когда они подъехали, оказалось, что у каждого водителя такси свой тариф за 1 километр.
#
# Директор знает, какому сотруднику сколько километров от работы до дома (к сожалению, все сотрудники живут в разных направлениях, поэтому нельзя отправить двух сотрудников на одной машине). Теперь директор хочет определить, сколько придется заплатить за перевозку всех сотрудников. Естественно, директор хочет заплатить как можно меньшую сумму.
#
# Входные данные
# В первой строке записаны N чисел через пробел, задающих расстояния в километрах от работы до домов сотрудников компании. Во второй строке записаны N чисел — тарифы за проезд одного километра в такси.
#
# Выходные данные
# Выведите одно целое число — наименьшую сумму, которую придется заплатить за доставку всех сотрудников.


def main():
    distance = sorted([int(s) for s in input().split()])
    traffic = sorted([int(s) for s in input().split()])[::-1]
    sum = 0
    for i in range(len(distance)):
        sum += distance[i] * traffic[i]
    print(sum)


if __name__ == '__main__':
    main()
