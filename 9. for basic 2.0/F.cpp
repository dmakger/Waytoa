/******************************************************************************

Задача №3536. Флаги
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n 
флагов. Изображение одного флага имеет размер 4×4 символов, между двумя 
соседними флагами также имеется пустой (из пробелов) столбец. Разрешается 
вывести пустой столбец после последнего флага. Внутри каждого флага должен 
быть записан его номер — число от 1 до n.

Входные данные
Вводится натуральное число.

Выходные данные
Выведите ответ на задачу.



+___ 
|1 / 
|__\ 
|  

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    const int LEN_FLAG = 4;
    string flag[LEN_FLAG] = {
        "+___",
        "|%d /",
        "|__\\",
        "|   ",
    };
    
    unsigned int d;
    cin >> d;
    for (int i = 0; i < LEN_FLAG; i++) {
        for (int j = 0; j < d; j++) {
            if (i == 1)
                printf("|%d / ", j + 1);
            else
                printf("%s ", flag[i].c_str());
        }
        printf("\n");
    }

    return 0;
}