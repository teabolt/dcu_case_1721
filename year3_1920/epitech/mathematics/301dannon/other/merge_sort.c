#include <stdio.h>
#include <stdlib.h>


void print_list(double list[], int N) {
    for (int i = 0; i < N; i++) {
        printf("%g, ", list[i]);
    }
    printf("\n");
}


void merge(double list[], int lo, int mid, int hi) {
    int left_size = mid-lo+1;
    double left[left_size];
    int right_size = hi-mid;
    double right[right_size];
    // printf("left: %d, right: %d\n", left_size, right_size);
    // printf("params: %d %d %d\n", lo, mid, hi);

    // TODO: in-place implementation?
    for (int i = 0; i < left_size; i++) {
        left[i] = list[lo+i];
    }
    for (int i = 0; i < right_size; i++) {
        right[i] = list[mid+1+i];
    }

    // print_list(left, left_size);
    // print_list(right, right_size);

    int i = 0;
    int j = 0;
    int k = lo;
    while (i < left_size && j < right_size) {
        if (left[i] <= right[j]) {
            list[k] = left[i];
            i++;
        } else {
            list[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < left_size) {
        list[k] = left[i];
        i++;
        k++;
    }
    while (j < right_size) {
        list[k] = right[j];
        j++;
        k++;
    }
    // print_list(list, 21);
}


// top down implementation
void merge_sort(double list[], int lo, int hi) {
    // lo included, hi excluded
    // printf("%d %d\n", lo, hi);
    if (lo < hi) {
        // recursive case
        int mid = (lo+hi)/2;
        // printf("lo %d hi %d mid %d\n", lo, hi, mid);
        merge_sort(list, lo, mid);
        merge_sort(list, mid+1, hi);
        // printf("going up recursion\n");
        merge(list, lo, mid, hi);
    }
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        return 84;
    } else {
        int N = 21;
        double list[] = {-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506,
                          306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339};
        print_list(list, N);
        merge_sort(list, 0, N-1);
        print_list(list, N);
        return 0;
    }
}