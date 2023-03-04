# Задача №119. Количество палиндромов
# Назовем число палиндромом, если оно не меняется при перестановке его цифр в обратном порядке.
# Напишите программу, которая по заданному числу K выводит количество натуральных палиндромов, не превосходящих K.
#
# Входные данные
# Задано единственное число K (1≤K≤100000).
#
# Выходные данные
# Необходимо вывести количество натуральных палиндромов, не превосходящих K.

def is_palindrome(digit: int):
    return str(digit) == str(digit)[::-1]


def count_palindrome(digit: int):
    return len([x for x in range(1, digit + 1) if is_palindrome(x)])


def main():
    print(count_palindrome(int(input())))


if __name__ == '__main__':
    main()
