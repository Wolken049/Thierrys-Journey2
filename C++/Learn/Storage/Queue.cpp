#include <iostream>
#include <queue>
using namespace std;

int main() {

    queue<char> letters;

    letters.push('A');
    letters.push('B');
    letters.push('C');
    letters.push('D');
    letters.push('E');

    letters.pop();

    cout << letters.front();
    return 0;
}