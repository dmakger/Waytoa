/******************************************************************************

Задача №3535. Пингвины
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n 
пингвинов. Изображение одного пингвина имеет размер 5×9 символов, между двумя 
соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается 
вывести пустой столбец после последнего пингвина. Для упрощения рисования 
скопируйте пингвина из примера в среду разработки.

Входные данные
Вводится натуральное число.

Выходные данные
Выведите ответ на задачу.

Примечание
Учтите, что вывод данных на экран производится построчно, а не попингвинно.

В некоторых языках программирования символ обратного слэша “\” в текстовых 
строках имеет специальное значение. Чтобы включить в состав текстовой строки 
такой символ, его нужно повторить дважды. Например, для вывода на экран одного 
такого символа можно использовать такой код: print("\\").

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    const int LEN_PENGUIN = 5;
    string penguin[LEN_PENGUIN] = {
        "   _~_    ",
        "  (o o)   ",
        " /  V  \\  ",
        "/(  _  )\\ ",
        "  ^^ ^^   "
    };
    
    unsigned int d;
    cin >> d;
    
    for (int i = 0; i < LEN_PENGUIN; i++) {
        for (int j = 0; j < d; j++) {
            cout << penguin[i];
        }
        cout << endl;
    }

    return 0;
}