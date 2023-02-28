# Задача №111336. Шифр Цезаря - 2
# Зашифруйте данный текстовый файл шифром Цезаря, при этом символы первой строки
# файла должны циклически сдвигаться на 1, второй строки — на 2, третьей строки — на три и т.д.
#
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
#
# Входные данные
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы латинского алфавита.
#
# Выходные данные
# Программа должна вывести шифрованные строчки

def main():
    with open('input.txt', 'r') as fin:
        shift = 1
        count_letter = 26
        for line in fin:
            word = ''
            for ch in line.split('\n')[0]:
                if str.isalpha(ch):
                    start_symbol = 'a'
                    if ch.isupper():
                        start_symbol = start_symbol.upper()

                    new_ch = chr(ord(start_symbol) + (ord(ch) - ord(start_symbol) + shift) % count_letter)
                    word += new_ch
                else:
                    word += ch
            print(word)
            shift += 1


if __name__ == '__main__':
    main()
