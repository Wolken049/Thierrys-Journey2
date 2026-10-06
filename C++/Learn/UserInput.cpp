#include <iostream>
using namespace std;

void String() {
    string x;
    cout << "Input Name here: ";
    cin >> x;
    cout << x;
}


void Integer() {
    int x;
    cout << "Input a Number here: ";
    cin >> x;
    cout << "Your Number: " << x;
}

int main() {
    Integer();
    String();
}