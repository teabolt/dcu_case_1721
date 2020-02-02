#include <stdio.h>
#include "utils.h"

/* Utility functions */


void print_list(double list[], int N) {
    // TODO: better way to print list?
    for (int i = 0; i < N; i++) {
        printf("%f, ", list[i]);
    }
    printf("\n");
}
