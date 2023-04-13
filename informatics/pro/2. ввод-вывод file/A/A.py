# Задача №111326. A + B
# Во входном файле записано два целых числа, каждое в отдельной строке. Выведите в выходной файл их сумму

def main():
    with open('input.txt', 'r') as fin:
        summ = 0
        for i in fin:
            summ += int(i)

        with open('output.txt', 'w') as fout:
            fout.write(str(summ))


if __name__ == '__main__':
    main()
