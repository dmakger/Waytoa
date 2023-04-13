# Задача №3552. Треугольная последовательность
# Дана монотонная последовательность, в которой каждое натуральное число k встречается ровно
# k раз: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...
#
# По данному натуральному n выведите первые n членов этой последовательности. Попробуйте обойтись только
# одним циклом for.
#
# Входные данные
# Вводится натурально число n.
#
# Выходные данные
# Выведите ответ на задачу.


def main():
    n = int(input())
    count = 0
    el = 1
    while count < n:
        for _ in range(el):
            if count >= n:
                break
            print(el, end=" ")
            count += 1
        el += 1


if __name__ == '__main__':
    main()
