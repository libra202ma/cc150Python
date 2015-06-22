/*

Write an aligned malloc and free function that supports allocating
memory such that the memory address returned is divisible by a
specific power of two.

EXAMPLE

align_malloc(1000, 128) will return a memory address that is a
multiple of 128 and that points to memory of size 1000 bytes.

aligned_free() will free memory allocated by align_malloc.

Allocate enough memory such that it will hold the data, and there
exist a starting point that could be divided by power of two.

The problem is that how to free the unused memories. `realloc` and
then `free`?

The reference answer given another solution. Store the original
pointer just before the start of aligned memory.

*/

#include <cstdlib>
#include <iostream>

using namespace std;

void* aligned_malloc(size_t size, int align) {
    void* ptr = (void *)malloc(size + align - 1 + sizeof(void*));
    if (ptr == NULL) {
        return NULL;
    }

    // find the aligned address
    /* void* aligned_ptr = (void**)ptr; */
    /* while ((size_t)aligned_ptr % align != 0) { */
    /*     aligned_ptr++; */
    /* } */

    cout << hex;
    cout << "Ptr: \t\t" << ptr << endl;

    // or more tricky one
    void** aligned_ptr = (void**)(((size_t)ptr + align - 1 + sizeof(void*)) & ~(align - 1));
    // which means moving back the highest address such that the last
    // few digits is 0s, i.e., divisible by power of 2.

    // store original pointer, that's why the aligned_ptr is declared
    // as void**
    aligned_ptr[-1] = ptr;

    cout << "Aligned_Ptr: \t" << aligned_ptr << endl;

    return (void*)aligned_ptr;
}

void align_free(void* ptr) {
    free(((void**)ptr)[-1]);
}

int main() {
    int *arr = (int*)aligned_malloc(100, 256);

    return 0;
}



/* Local Variables: */
/* compile-command: "c++ 13_09.cpp -o 13_09 && ./13_09" */
/* End: */
