#include <iostream>

using namespace std;


int main() {
    int a, b;
    cin >> a >> b;

    for (int digit = a; digit <= b; digit++) {
        if (digit % 2 == 0)
            cout << digit << ' ';
    }

    return 0;
}