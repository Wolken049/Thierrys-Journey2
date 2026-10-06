#include <iostream>
#include <stack>
using namespace std;

int main() {

    stack<char> letters;

    letters.push('A');
    letters.push('B');
    letters.push('C');
    letters.push('D');
    letters.push('E');

    letters.pop();

    cout << letters.top();
    return 0;
}