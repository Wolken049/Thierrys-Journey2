#include <stdio.h>

int main(){
    const int arr[][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}

    };
    int i;
    int j;
    int size = sizeof(arr) / sizeof(arr[0]);

    printf("2D: ");
    for (i = 0; i < size; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d ", arr[i][j]);
        }
    }
}
