#include <stdio.h>

//Constants
#define Size 5

//Variables
int Queue[Size] = {0};
int HeadPointer = -1;
int TailPointer = -1;

int Enqueue(int Element) {
    if (HeadPointer == Size - 1) {
        return -1;
    } else {
        HeadPointer += 1;
        Queue[HeadPointer] = Element;
        return 1;
    }
}

int Dequeue() {
    int Value;

    if (HeadPointer == TailPointer) {
        return -1;
    } else {
        TailPointer += 1;
        Value = Queue[TailPointer];
        Queue[TailPointer] = 0;
        return Value;
    }
}


int main() {
    int i;
    int j;
    int Queued = Enqueue(10);

    Queued = Enqueue(5);
    Queued = Enqueue(1);
    Queued = Enqueue(3);
    Queued = Enqueue(2);

    int Dequeued = Dequeue();

    while (Dequeued != -1) {
        printf("%i ", Dequeued);
        Dequeued = Dequeue();
    }

    printf("\nDone");

    return 0;
}
