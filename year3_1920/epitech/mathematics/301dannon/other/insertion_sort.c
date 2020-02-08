#include <stdio.h>
// #include "utils.h"


// FIXME: utils.h
void print_list(double list[], int N) {
    // TODO: better way to print list?
    for (int i = 0; i < N; i++) {
        printf("%g, ", list[i]);
    }
    printf("\n");
}


void swap(double list[], int i, int j) {
    double tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
}


void insertion_sort(double list[], int N) {
    // iterate through each element
    // start from 2nd element (micro-optimization)
    for (int i = 1; i < N; i++) {
        double v = list[i]; // TODO: solution where you don't have to remember the element?
        // iterate backwards until find where element belongs
        for (int j = i-1; 0 <= j; j--) {
            if (list[j] <= v) {
                break;
            } else {
                swap(list, j+1, j); // TODO: solution with shifting instead of swapping
            }
        }

        // TODO: solution with linear search loop
        // int j = i - 1;
        // while (0 <= j && list[i] < list[j]) {
        //     // if smaller, keep going (if equal or greater, stop)
        //     // shift values to make room
        //     // TODO: assign vs swap
        //     list[j+1] = list[j];
        //     j -= 1;
        // }
        // printf("%d\n", j);
        // if (0 <= j) {
        //     list[j] = v;
        // } else {
        //     list[0] = v;
        // }
    }
}


int main() {
    int N = 5;
    double list[] = {3, -3.4, -5, 0, 2.1};
    print_list(list, N);
    insertion_sort(list, N);
    print_list(list, N);
    return 0;
}