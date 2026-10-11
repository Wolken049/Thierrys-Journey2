#include <stdio.h>

int main() {
    const int Arr[] = {2, 5, 6, 2, 4, 1, 5, 2, 1, 6,};
    int i;
    const int Length = sizeof(Arr) / sizeof(Arr[0]);

    for (i = 0; i < Length; i++) {
        printf("%i ", Arr[i]);
    }

    return 0;
}
