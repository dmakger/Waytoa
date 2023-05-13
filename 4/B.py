# Вам дается специальный пазл, состоящий из n⋅m одинаковых деталей. Каждая деталь имеет три выступа и одну
# выемку, как показано на рисунке.
#
#
# Пазл считается собранным, если следующие условия выполнены:
#
# Детали расположены в виде прямоугольника с n строками и m столбцами.
# Любые две детали, которые имеют общую сторону в прямоугольнике, идеально соединяются с помощью выступа одной
# детали и выемки другой.
# Определите, можно ли собрать пазл, вращая и перемещая детали как угодно.
#
# Входные данные
# Каждый тест содержит несколько тестовых случаев. В первой строке находится единственное целое число t
# (1≤t≤1000) — количество тестовых случаев. В следующих t строках следует описание тестовых случаев.
#
# Единственная строка описания каждого тестового случая содержит два целых числа n и m (1≤n,m≤105).
#
# Выходные данные
# Для каждого тестового случая выведите единственную строку, содержащую «YES», если возможно собрать пазл
# и «NO», иначе. Вы можете выводить каждый символ в любом регистре.

def get_result(n, m):
    if (n > 1 and m > 1) and not(n == 2 == m):
        return 'NO'
    return 'YES'


def main():
    for _ in range(int(input())):
        print(get_result(*map(int, input().split())))


if __name__ == '__main__':
    main()