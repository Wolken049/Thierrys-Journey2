#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int Element;
    struct Node *Next;
} Node;

Node *Root = NULL;
int Number = 0;

int ListAdd(int Element) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    Node *Current = NULL;
    if (newNode == NULL) {
        return 0;
    }

    if (Number == 20) {
        free(newNode);
        return 0;
    } else if (Number == 0) {
        newNode->Element = Element;
        newNode->Next = NULL;
        Root = newNode;
        Number = 1;
        printf("Passed\n");
        return 1;
    } else {
        newNode->Element = Element;
        newNode->Next = NULL;
        Current = Root;
        int Count = 0;
        while (Current->Next != NULL && Count <= Number) {
            Current = Current->Next;
            Count += 1;
        }
        if (Count >= 100) {
            printf("Error");
            free(newNode);
            return 0;
        }
        Current->Next = newNode;
        Number += 1;
        printf("Passed\n");
        return 1;
    }
}

int Traverse() {
    Node *Current = NULL;
    if (Root == NULL) {
        return -1;
    }

    Current = Root;
    while (Current != NULL) {
        printf("%d\n", Current->Element);
        Current = Current->Next;
    }
    return 1;
}

int Remove(int Target) {
    Node *Previous = NULL;
    Node *Current = NULL;
    if (Root == NULL) {
        return -1;
    }

    Current = Root;
    int Count = 0;
    Node *temp = NULL;
    while (Current != NULL && Count <= 100) {
        if (Current->Element == Target) {
            if (Current->Next == NULL) {
                free(Current);
                return 1;
            } else {
                temp = Current->Next;
                Previous->Next = temp;
                free(Current);
                return 1;
            }
        } else {
            Previous = Current;
            Current = Current->Next;
            Count += 1;
        }
    }
    return 0;
}

int main() {

    ListAdd(1);
    ListAdd(2);
    ListAdd(3);
    ListAdd(4);
    ListAdd(5);

    printf("Before: \n");
    Traverse();

    Remove(3);

    printf("After: \n");
    Traverse();

    int Try = Remove(9);
    if (Try == 0) {
        printf("Not in List");
    }

    return 0;
}
