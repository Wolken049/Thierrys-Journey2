#include <stdio.h>
#include <stdlib.h>

int main() {
    int *students;
    int numStudents = 12;
    students = calloc(numStudents, sizeof(*students));
    printf("%zu\n", numStudents * sizeof(*students));


    *students = 2;
    students[1] = 4;
    students[2] = 6;

    printf("%d\n", *students);
    printf("%d %d %d \n", students[1], students[2], students[3]);


    free(students);

    return 0;
}
