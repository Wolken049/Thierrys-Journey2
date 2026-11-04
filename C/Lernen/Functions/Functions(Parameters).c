#include <stdio.h>

int Addition(int x, int y) {
    int z = x + y;
    return z;
}

int main(){
    int x = 1;
    int y = 1;

    int Value = Addition(x, y);

    printf("%i", Value);

    return 0;
}
