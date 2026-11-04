#include <stdio.h>

int Stack[5] = {0, 0, 0, 0, 0};
int top = -1;
int size = 5;

int push(int Element) {
    if (top == (size - 1)) {
        return -1;
    } else {
        top = top + 1;
        Stack[top] = Element;
        return 1;
    }
}

int pop() {
    if (top == -1) {
        return -1;
    } else {
        int Value = Stack[top];
        Stack[top] = 0;
        top = top - 1;
        return Value;
    }
}

int main() {
    int Pushed = push(10);
    int i;
    int j;

    if (Pushed == -1) {
        printf("Stack is full\n");
    } else {
        printf("Number has been pushed\n");
    }

    int Popped = pop();

    if (Popped == -1) {
        printf("Stack is Empty\n");
    } else {
        printf("Removed: %i\n", Popped);
    }

    return 0;

}
