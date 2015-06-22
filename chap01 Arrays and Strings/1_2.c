/*
Implement a function void reverse(char* str) in C or C++ which reverse
a null-terminated string.

- naive. swap characters one by one except the last null character \0.
*/

#include <stdio.h>
#include <stdlib.h>
#include "1_2.h"

void reverse(char* s) {
    int j = 0;
    while (s[j] != '\0') {
        j++;
    } // now j point to \0, end of the string
    j--;

    int i = 0;
    char tmp;
    while (i < j) {
        tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
        i++;
        j--;
    }
}
