# Задача №111331. Длинные строки
# В выходной файл выведите все строки наибольшей длины из входного файла, не меняя их порядок.
#
# В данной задаче удобно считать список строк входного файла целиком при помощи метода readlines().

def main():
    with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
        d = dict()
        for s in fin.readlines():
            s_result = s.split('\n')[0]
            size_s_result = len(s_result)
            if d.get(size_s_result) is None:
                d[size_s_result] = []
            d[size_s_result].append(s_result)

        max_size = max(d.keys())
        fout.write('\n'.join(d[max_size]))



if __name__ == '__main__':
    main()
