#include <stdio.h>

int LinearSearch(int arr[], int size, int target) {
    int i;
    for (i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    int arr[] = {4, 8, 1, 6, 0, 2, 3, 9, 5, 7};
    int length = sizeof(arr) / sizeof(arr[0]);

    int Location = LinearSearch(arr, length ,0);

    if (Location == -1) {
        printf("Number not found");
    } else {
        printf("Number found in: %i", Location);
    }
}
