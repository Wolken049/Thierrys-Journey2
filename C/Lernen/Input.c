#include <stdio.h>


int main() {
    char Name[30];
    int Age;


    printf("Please enter your name: ");
    scanf("%29s", Name);

    printf("Please enter your age: ");
    scanf("%d",&Age);

    if (Age == 1) {
        printf("So you're name is %s and you're %i year old", Name, Age);
    } else {
        printf("So you're name is %s and you're %i years old", Name, Age);
    }

    return 0;
}
