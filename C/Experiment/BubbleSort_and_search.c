#include <stdio.h>

int BubbleSort(int arr[], int size) {
    int i;
    int j;
    int temp;


    if (size == 1){
        return 0;
    } else {
        for (i = 0; i < size; i++) {
            for (j = 0; j < (size-i-1); j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    return 1;
}

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

    return 0;
}


int main() {
    int sinarr[] = {2};
    int unsortedarr[] = {4, 2, 1, 5, 9, 6, 8, 3, 7, 0};
    int sinsize = sizeof(sinarr) / sizeof(sinarr[0]);
    int ussize = sizeof(unsortedarr) / sizeof(unsortedarr[0]);

    int Testsin = BubbleSort(sinarr, sinsize);
    int Testunsort = BubbleSort(unsortedarr, ussize);

    if (Testsin == 0) {
        printf("That's just a variable: %i\n", sinarr[0]);
    } else {
        printf("Was ist los??");
    }

    if (Testunsort == 1) {
        int target = 4;
        int find = BinarySearch(unsortedarr, ussize, target);
        if (find == 0) {
            printf("Warum hat sie die Nummer nicht gefunden?");
        } else {
            printf("Found %i in position: %i\n", target, find);
        }
    } else {
        printf("Boah und ich hab viel geschrieben");
    }

    return 0;
}
