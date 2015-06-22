/*

Write a function in C called my2DAlloc which allocates a
two-dimensional array. Minimize the number of calls to malloc and make
sure the memory is accessible by the notation arr[i][j].

To ensure data could be accessed using arr[i][j], arr[i] shall be
pointer to array, arr shall be pointer to array which composed by
pointers to array. The content of arr could be filled by using results
from malloc individually. Or to minimize of calls of malloc, the data
block could be allocated once, and the row address could be obtained
by pointer arithmetic.

*/

#include <stdio.h>
#include <stdlib.h>

int** my2DAlloc(int m, int n) {
    // malloc row pointers
    int** ptr = (int**)malloc(sizeof(int*) * m);
    if (ptr == NULL) {
        return NULL;
    }
    // malloc data
    int* data = (int*)malloc(sizeof(int) * m * n);
    if (data == NULL) {
        return NULL;
    }

    // or we might use malloc only once, but that would less
    // obvious. But it does has benefit, the free process would be
    // easier.

    // assign row pointers
    for (int i = 0; i < m; i++) {
        ptr[i] = data + i * n;
    }

    return ptr;
}

int main() {
    int m = 2;
    int n = 2;
    int** mat = my2DAlloc(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }

    // free memories
    free(*mat);
    free(mat);
    return 0;
}

/* Local Variables: */
/* compile-command: "cc 13_10.c -o 13_10 && ./13_10" */
/* End: */
