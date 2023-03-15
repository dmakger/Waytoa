//Задача №340. Делители числа
//Выведите все натуральные делители числа x в порядке возрастания (включая 1 и само число).
//
//Входные данные
//Вводится натуральное число x
//
//Выходные данные
//Выведите все делители числа x

#include <iostream>

using namespace std;


int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (n % i == 0)
            cout << i << ' ';
    }

    return 0;
}