#include <stdio.h>
#include <stdbool.h>

bool Switch(bool x) {
    if (x == true) {
        x = false;
    } else {
        x = true;
    }
    return x;
}

int main() {
    bool val = false;
    bool Switched = Switch(val);

    printf("%d", Switched);

    return 0;
}
