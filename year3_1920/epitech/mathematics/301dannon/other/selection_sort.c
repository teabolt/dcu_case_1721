#include <stdio.h>


// BIGTODO'S:
// * benchmark (count number of comparisons)


// TODO: utility file?
void swap(int list[], int i, int j) {
    // TODO: better swap in C?
    int tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
}


// TODO: existing function from standard library?
int minimum(int list[], int start, int end) {
    // return index of minimum element in a list in range start inclusive to end exclusive
    // we assume that n is at most the number of elements in the list
    int guess = start;
    for (int i = start+1; i < end; i++) {
        if (list[i] < list[guess]) {
            guess = i;
        }
    }
    return guess;
}


void selection_sort(int list[], int N) {
    // go through each "unsorted" entry
    for (int i = 0; i < N-1; i++) {
        // leave out the very last entry as it will be in order (micro-optimization)
        // find minimum in unsorted and swap "unsorted" with minimum
        int j = minimum(list, i, N);
        swap(list, i, j);
        // TODO: optimization - only swap if i != j (element not already in place)
    }
}


void print_list(int list[], int N) {
    // TODO: better way to print list?
    for (int i = 0; i < N; i++) {
        printf("%d, ", list[i]);
    }
    printf("\n");
}


int main() {
    // TODO: make code generic (work with double, then any comparable type not just int)
    int list[6] = {1, -4, 5, 3, 5, 7};
    // printf(list);
    int size = 6;
    print_list(list, size);
    selection_sort(list, size);
    print_list(list, size);
    // TODO: count operations / benchmarking approach?
    return 0;
}