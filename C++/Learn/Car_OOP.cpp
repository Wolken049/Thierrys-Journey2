#include <iostream>
using namespace std;

class Car {
    public:
        string brand;
        string model;
        int year;
};

int main() {
    Car carObj1;
    carObj1.brand = "Benz";
    carObj1.model = "C-280";
    carObj1.year = 2007;

    Car carObj2;
    carObj2.brand = "Ford";
    carObj2.model = "Mustang";
    carObj2.year = 1969;

    cout << carObj1.brand << " " << carObj1.model << " " << carObj1.year << "\n";
    cout << carObj2.brand << " " << carObj2.model << " " << carObj2.year << "\n";
    return 0;
}