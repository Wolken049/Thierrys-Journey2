#include <stdio.h>
#include <string.h>

int main() {
    const char myName[] = "Thierry";

    if (strcmp(myName, "Thierry") == 0) {
        printf("Welcome");
    }
    else {
        printf("Who are you?");
    }
    return 0;
}
