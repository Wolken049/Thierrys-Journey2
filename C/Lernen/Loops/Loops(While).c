#include <stdio.h>

int main() {
    int Count = 0;
    const int goal = 10;

    while (Count < goal) {
        printf("%i, ", Count, "/n");
        Count = Count++;
    }
}
