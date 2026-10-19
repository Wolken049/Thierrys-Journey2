#include <stdio.h>

void Insert_sort(int Arr[], int Size) {
    int Count;
    int Insert;
    int Key;

    for (Count = 0; Count < Size; Count++) {
        Key = Arr[Count];
        Insert = Count - 1;
        while (Insert >= 0 && Arr[Insert] > Key) {
            Arr[Insert + 1] = Arr[Insert];
            Insert -= 1;
        }
        Arr[Insert + 1] = Key;
    }
}

int main(void) {
    int Arr[] = {8, 6, 4, 3, 5, 1, 2, 0, 9, 7};
    const int Size = sizeof(Arr) / sizeof(Arr[0]) - 1;
    int i;

    Insert_sort(Arr, Size);

    for (i = 0; i < Size; i++) {
        if (i != Size - 1) {
            printf("%d, ", Arr[i]);
        } else {
            printf("%d", Arr[i]);
        }
    }

}
