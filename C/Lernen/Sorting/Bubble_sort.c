#include <stdio.h>

int main() {
    int Arr[] = {4, 2, 8, 9, 5, 1, 7, 3, 6, 0};
    int n = sizeof(Arr) / sizeof(Arr[0]);
    int i;
    int j;
    int k;
    int Temp;

    for (i = 0; i < n; i++) {
        for (j = 0; j < (n-i-1); j++) {
            if (Arr[j] > Arr[j + 1]) {
                Temp = Arr[j];
                Arr[j] = Arr[j + 1];
                Arr[j + 1] = Temp;
            }
        }
    }

    for (k = 0; k < n; k++) {
        printf("%i ", Arr[k]);
    }

    return 0;
}
