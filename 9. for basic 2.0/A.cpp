/******************************************************************************

Задача №112202. Произведение
Напишите программу, которая вводит два целых числа и находит их произведение, 
не используя операцию умножения. Учтите, что числа могут быть отрицательными.

Входные данные
Входная строка содержит два целых числа.

Выходные данные
Программа должна вывести произведение введённых чисел.

*******************************************************************************/
#include <iostream>
#include <math.h>


using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    
    unsigned int aAbs, bAbs;
    aAbs = abs(a);
    bAbs = abs(b);
    
    int result = 0;
    for (int i = 0; i < aAbs; ++i) {
        result += bAbs;
    }
    
    if (((a < 0) or (b < 0)) and not ((a < 0) and (b < 0)))
        result = 0 - result;
    cout << result;

    return 0;
}