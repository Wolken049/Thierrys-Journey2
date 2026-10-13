#include <stdio.h>

int main() {
    const int arr[4] = {24, 2, 17, 2};
    int i;
    int* ptr;

    for (i = 0; i < 4; i++) {
        ptr = &arr[i];
        printf("Adress: %d\n", &arr[i]);
        printf("Pointer: %p\n", ptr);
    }

    return 0;
}
