#include <stdio.h>

int main() {
    const int Battery = 30;
    if (Battery == 0) {
        printf("Dead Battery");
    }
    else if (Battery <= 10 ) {
        printf("Critical battery");
    } else if (Battery <= 25) {
        printf("Low Battery");
    } else if (Battery <= 50) {
        printf("SubOpt Battery");
    } else {
        printf("Normal Battery");
    }

    return 0;
}
