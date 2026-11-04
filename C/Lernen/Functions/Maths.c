#include <stdio.h>
#include <math.h>

int main() {
    int base = 4;
    float rounding = 4.5;

    printf("The square root of %i is %f\n", base, sqrt(base));
    printf("Rounding up %f is %f\n", rounding, ceil(rounding));
    printf("Rounding down %f is %f\n", rounding, floor(rounding));

    return 0;
}
