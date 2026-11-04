#include <stdio.h>

int main() {
    FILE *fptr = fopen("nothing.txt", "r");

    if (fptr == NULL) {
        fprintf(stderr, "Error: FIle not Found\n");
        return 1;
    }

    fclose(fptr);
    return 0;

}
