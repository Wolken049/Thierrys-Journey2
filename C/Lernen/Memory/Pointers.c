#include <stdio.h>

int main() {
    const int myAge= 19;
    const int* ptr = &myAge;

    printf("%d\n", myAge);
    printf("%p\n", myAge);
    printf("%p\n", ptr);

    return 0;
}
