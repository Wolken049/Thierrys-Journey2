#include <stdio.h>



int main() {
    //Declaring Variables
    int myNumbers[] =  {64, 34, 25, 12, 22, 11, 90, 5, 11, 12, 34, 22, 67, 43, 27, 87, 92, 56, 32};
    int key;
    int Insert;
    int i;
    int length = sizeof(myNumbers) / sizeof(myNumbers[0]);

    for (i = 0; i<length; i++) {
        key = myNumbers[i];
        Insert = i - 1;
        while (Insert >= 0 && myNumbers[Insert] > key) {
            myNumbers[Insert + 1] = myNumbers[Insert];
            Insert = Insert - 1;
        }
        myNumbers[Insert + 1] = key;
        Insert = Insert - 1;
    }
    // Print sorted array
    printf("Sorted array:\n");
    for (i = 0; i < length; i++) {
        printf("%d ", myNumbers[i]);
    }
    printf("\n");

    return 0;

    return 0;
}
