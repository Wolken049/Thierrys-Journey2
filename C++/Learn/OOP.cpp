#include <iostream>
using namespace std;

class MyClass {
    public:
        int myNumb;
        string myString;
};

int main() {
    MyClass myObj;

    myObj.myNumb = 15;
    myObj.myString = "Some text";

    cout << myObj.myNumb << "\n";
    cout << myObj.myString;
    return 0;
}