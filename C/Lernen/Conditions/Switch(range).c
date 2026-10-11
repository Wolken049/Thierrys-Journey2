#include <stdio.h>

int main() {
    const int Percent = 40;
    char Grade;

    switch (Percent) {
        case 0 ... 39:
            Grade = 'U';
            break;
        case 40 ... 49:
            Grade = 'E';
            break;
        case 50 ... 59:
            Grade = 'D';
            break;
        case 60 ... 69:
            Grade = 'C';
            break;
        case 70 ... 79:
            Grade = 'B';
            break;
        case 80 ... 89:
            Grade = 'A';
            break;
        case 90 ... 100:
            Grade = 'S';
            break;
    }
    printf("They have received grade: %c", Grade);

    return 0;
}
