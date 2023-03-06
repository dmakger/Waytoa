#include <iostream>

using namespace std;


int main() {
    int a, b;
    cin >> a >> b;

    for (int digit = a; digit <= b; digit++) {
        cout << digit << ' ';
    }

    return 0;
}