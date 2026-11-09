#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int Element;
    struct Node *Next
} Node;

Node *Root = NULL;
int Number = 0;

int ListAdd(int Element) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    Node *Parent = NULL;
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
        printf("Passed First\n");
        return 1;
    } else {
        newNode->Element = Element;
        newNode->Next = NULL;
        Current = Root;
        int Count = 0;
        while (Current != NULL && Current->Element < newNode->Element && Count <= Number) {
            Parent = Current;
            Current = Current->Next;
            Count += 1;
        }
        if (Count > Number) {
            printf("Not Passed\n");
            free(newNode);
            return 0;
        }
        if (Parent->Next == NULL) {
            Parent->Next = newNode;
        } else {
            Current = Parent->Next;
            newNode->Next = Current;
            Parent->Next = newNode;
        }
        Number += 1;
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




int main() {

    ListAdd(1);
    ListAdd(2);
    ListAdd(4);

    printf("Traverse First\n");
    Traverse();

    ListAdd(3);

    printf("Traverse Updated\n");
    Traverse();

    return 0;

}


