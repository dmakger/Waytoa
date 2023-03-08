#include <iostream>

using namespace std;


int main() {
    int a, b;
    cin >> a >> b;

    int digit = a + a % 2;
    for (;digit <= b; digit+=2) {
        cout << digit << ' ';
    }

    return 0;
}