#include <iostream>
using namespace std;

int main () {
    int x;
    int y;
    
    x = 20;
    y = 22;
    if (x > y) {
        cout << "x is greater than y";
    } else if (x == y) {
        cout << "x is equal to y";
    } else {
        cout << "x is less than y";
    }
}
