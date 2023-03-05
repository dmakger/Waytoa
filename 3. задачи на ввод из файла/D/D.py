# Задача №111334. Сумма чисел в файле
# В файле могут быть записаны десятичные цифры и все, что угодно.
# Числом назовем последовательность цифр, идущих подряд (т.е. число всегда неотрицательно).
#
# Вычислите сумму всех чисел, записанных в файле. В данной задаче удобно считывать данные посимвольно

def main():
    str_digits = '1234567890'
    with open('input.txt', 'r') as fin:
        is_complete = True
        summ = 0
        digit = ''
        while is_complete:
            ch = fin.read(1)
            if ch in str_digits:
                digit += ch
                if ch == '':
                    is_complete = False
            else:
                if digit != '':
                    summ += int(digit)
                    digit = ''
        print(summ)


if __name__ == '__main__':
    main()
