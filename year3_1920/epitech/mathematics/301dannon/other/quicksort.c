#include <stdio.h>
#include <stdlib.h>


void print_list(double list[], int N) {
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


int partition(double list[], int lo, int hi) {
    int pivot = lo;
    double v = list[pivot];

    int i = lo+1;
    int j = hi;

    while (i < j) {
        // left
        while (i < hi && list[i] < v) {
            i++;
        }

        // right
        while (j >= lo && list[j] >= v) {
            j--;
        }
        // printf("%d and %d\n", i, j);

        if (i < j) {
            swap(list, i, j);
        }
        // print_list(list, 21);
    }
    if (list[j] < v) {
        swap(list, pivot, j);
    }
    return j;
    // TODO: check correctness + simplify
}


void r_quicksort(double list[], int lo, int hi) {
    // printf("new iter: %d & %d\n", lo, hi);
    if (lo < hi) {
        int pivot = partition(list, lo, hi);
        // printf("%d\n", pivot);
        r_quicksort(list, lo, pivot-1);
        r_quicksort(list, pivot+1, hi);
    }
}


void quicksort(double list[], int N) {
    r_quicksort(list, 0, N-1);
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        return 84;
    } else {
        // FIXME
        // read_array(argv[1]);
        int N = 21;
        double list[] = {-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506,
                          306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339};
        print_list(list, N);
        quicksort(list, N);
        print_list(list, N);
        return 0;
    }
}