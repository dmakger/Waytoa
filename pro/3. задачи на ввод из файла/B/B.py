# Задача №111335. Статистика по файлу
# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# Выведите три найденных числа в формате, приведенном в примере.
#
# Для экономии памяти читайте файл посимвольно, то есть не сохраняя целиком в памяти
# файл или отдельные его строки

def main():

    with open('input.txt', 'r') as fin:
        is_complete = True
        letters_count = 0
        words_count = 0
        lines_count = 0
        last_ch = ''
        in_word = False
        while is_complete:
            ch = fin.read(1)
            if ch == '\n':
                lines_count += 1
                if in_word:
                    words_count += 1
                    in_word = False
            elif ch == ' ':
                words_count += 1
            elif ch == '':
                is_complete = False
                if in_word:
                    words_count += 1
                    in_word = False
                if last_ch != '\n':
                    lines_count += 1
            else:
                in_word = True
                if str.isalpha(ch):
                    letters_count += 1
            last_ch = ch

        print('Input file contains:\n'
              f'{letters_count} letters\n'
              f'{words_count} words\n'
              f'{lines_count} lines\n')


if __name__ == '__main__':
    main()
