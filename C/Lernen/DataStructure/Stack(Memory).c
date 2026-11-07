#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int Element;
    struct Node *Next;
} Node;

Node *Top = NULL;
int Number = 0;

int Push(int Element) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) {
        return 0;
    }

    newNode->Element = Element;
    newNode->Next = Top;
    Top = newNode;
    Number += 1;

    return 1;
}

int Pop() {
    if (Top == NULL) {
        return 0;
    }

    Node *temp = Top;
    int Value = temp->Element;

    Top = Top->Next;
    free(temp);
    Number -= 1;
    return Value;


}

int main() {

    Push(12);
    Push(99);

    int Value = Pop();

    while (Value != 0) {
        printf("%d\n", Value);
        Value = Pop();
    }

    return 0;
}
