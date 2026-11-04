#include <stdio.h>

int BinarySearch(int arr[], int size, int target) {
    int lower = 0;
    int upper = size - 1;

    while (lower <= upper) {
        int middle = (lower + upper) / 2;

        if (arr[middle] == target) {
            return middle;
        } else if (arr[middle] < target) {
            lower = middle + 1;
        } else {
            upper = middle - 1;
        }
    }

    return -1;
}

int main() {
    int arr[] = {1, 3, 4, 6, 9, 11, 15, 18};
    int size = sizeof(arr) / sizeof(arr[0]);

    int Within = BinarySearch(arr, size, 6);
    int Lowlimit = BinarySearch(arr, size, 1);
    int Highlimit = BinarySearch(arr, size, 18);
    int Outside = BinarySearch(arr, size, 20);

    printf("6 was found in position %i\n", Within);
    printf("1 was found in position %i\n", Lowlimit);
    printf("18 was found in position %i\n", Highlimit);
    printf("20 was found in position %i\n", Outside); // fix this

    return 0;
}
