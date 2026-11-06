#include <stdio.h>

void printAge(int Age) {
    printf("You are %d years old\n", Age);
}

void printAgePoint(int *Age) {
    printf("The adress shows you are %d years old", *Age);
}

int main() {
    const int myAge= 19;
    const int *pAge = &myAge;

    printf("Adress of age: %p\n", &myAge);
    printf("value of pAge: %p\n", pAge);

    printf("Size of myAge: %d bytes\n", sizeof(myAge));
    printf("Size of pAge: %d bytes\n", sizeof(pAge));


    printf("Value of age: %d\n", myAge);
    printf("Value of stored address: %d\n", *pAge);

    printAge(myAge);
    printAgePoint(pAge);

    return 0;
}
