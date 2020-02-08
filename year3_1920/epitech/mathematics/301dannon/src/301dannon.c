#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

/*
* 301dannon - comparing sorting algorithms
* Baltrunas Tomas and Sanghun Moon.
*/


char* HELP = "USAGE\n"
             "    ./301dannon file\n"
             "DESCRIPTION\n"
             "    file    file that contains the numbers to be sorted, seperated by spaces\n";


void print_help() {
    printf("%s", HELP);
}


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


// Need a way to read an unknown amount of numbers into an arrray
// One solution - scan file twice
// First scan for number of elements.
// Secondly to read the elements into an allocated array.

// Another solution:
// Dynamically resize array or allocate memory


int find_elements_number(char* filename) {
    FILE *fp;
    fp = fopen(filename, "r");

    if (fp == NULL) {
        exit(84);
    }

    int N = 0;
    double num;
    while (fscanf(fp, "%lf", &num) == 1) {
        N++;
    }
    fclose(fp);

    return N;
}


void read_list(char* filename, double* list) {
    FILE *fp;
    fp = fopen(filename, "r");

    if (fp == NULL) {
        exit(84);
    }

    double num;
    int i = 0;
    while (fscanf(fp, "%lf", &num) == 1) {
        list[i] = num;
        i++;
    }
    fclose(fp);
}


// TODO: split all these sorts into separate files


// Merge sort
void merge(double list[], int lo, int mid, int hi, int* cmp_count) {
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
        *cmp_count += 1;
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
void merge_sort(double list[], int lo, int hi, int* cmp_count) {
    // lo included, hi excluded
    // printf("%d %d\n", lo, hi);
    if (lo < hi) {
        // recursive case
        int mid = (lo+hi)/2;
        // printf("lo %d hi %d mid %d\n", lo, hi, mid);
        merge_sort(list, lo, mid, cmp_count);
        merge_sort(list, mid+1, hi, cmp_count);
        // printf("going up recursion\n");
        merge(list, lo, mid, hi, cmp_count);
    }
}


// Quick sort
int partition(double list[], int lo, int hi, int* cmp_count) {
    int pivot = lo;
    double v = list[pivot];

    int i = lo+1;
    int j = hi;

    while (i < j) {
        // left
        while (i < hi && list[i] < v) {
            *cmp_count += 1;
            i++;
        }
        if (i < hi) *cmp_count += 1;

        // right
        while (j >= lo && list[j] >= v) {
            *cmp_count += 1;
            j--;
        }
        if (j >= lo) *cmp_count += 1;
        
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

void r_quicksort(double list[], int lo, int hi, int* cmp_count) {
    // printf("new iter: %d & %d\n", lo, hi);
    if (lo < hi) {
        int pivot = partition(list, lo, hi, cmp_count);
        // printf("%d\n", pivot);
        r_quicksort(list, lo, pivot-1, cmp_count);
        r_quicksort(list, pivot+1, hi, cmp_count);
    }
}

void quicksort(double list[], int N, int* cmp_count) {
    r_quicksort(list, 0, N-1, cmp_count);
}


// Bubble sort
int bubble_sort(double list[], int N) {
    int cmp_count = 0; 
    for (int i = N; 0 < i; i--) {
        // printf("%d\n", i);
        for (int j = 1; j < i; j++) {
            cmp_count += 1;
            if (list[j-1] > list[j]) {
                swap(list, j-1, j);
            }
            // printf("--> %d %d\n", j-1, j);
        }
    }
    return cmp_count;
}


// Insertion sort
int insertion_sort(double list[], int N) {
    int cmp_count = 0;

    // int i, j;
    // double key;
    // for (i = 1; i < N; i++) 
    // {  
    //     key = list[i];  
    //     j = i - 1;  
  
    //     /* Move elements of arr[0..i-1], that are  
    //     greater than key, to one position ahead  
    //     of their current position */
    //     while (j >= 0 && list[j] > key) 
    //     {
    //         cmp_count += 1;  
    //         list[j + 1] = list[j];  
    //         j = j - 1;  
    //     }
    //     if (j >= 0) cmp_count += 1;

    //     list[j + 1] = key;  
    // }  

    // iterate through each element
    // start from 2nd element (micro-optimization)
    for (int i = 1; i < N; i++) {
        double v = list[i]; // TODO: solution where you don't have to remember the element?
        // iterate backwards until find where element belongs
        for (int j = i-1; 0 <= j; j--) {
            cmp_count += 1;
            if (list[j] <= v) {
                break;
            } else {
                swap(list, j+1, j); // TODO: solution with shifting instead of swapping
            }
        }
    }
    return cmp_count;
}


// Selection sort
int selection_sort(double list[], int N) {
    // go through each "unsorted" entry
    int cmp_count = 0;
    for (int i = 0; i < N-1; i++) {
        // leave out the very last entry as it will be in order (micro-optimization)
        // find minimum in unsorted and swap "unsorted" with minimum
        int min = i;
        for (int j = i+1; j < N; j++) {
            cmp_count += 1;
            if (list[j] < list[min]) {
                min = j;
            }
        }
        swap(list, i, min);
        // TODO: optimization - only swap if i != j (element not already in place)
    }
    return cmp_count;
}


int main(int argc, char *argv[]) {
    int opt = getopt(argc, argv, "h");
    if (opt == 'h') {
        print_help();
        return 0;
    } else if (opt != -1) {
        // other argument
        return 84;
    }

    if (argc != 2) {
        // no file argument
        print_help();
        return 84;
    } else {
        char* filename = argv[1];

        // find how many elements we have
        int N = find_elements_number(filename);

        if (N == 0) {
            // empty list
            return 84;
        }

        if (N == 1) {
            // change plural to singular
            // TODO: better if statement (only change "element")
            printf("%d element\n", N);
        } else {
            printf("%d elements\n", N);
        }

        // read file contents into an array
        double list[N];
        read_list(filename, list);
        
        int cmp_count;

        // make a copy of the unsorted list
        // this is because the sorting algorithms modify the passed list
        double sorted[N];
        memcpy(sorted, list, N * sizeof*list);
        cmp_count = selection_sort(sorted, N);
        printf("Selection sort: %d comparisons\n", cmp_count);
        // print_list(sorted, N);

        memcpy(sorted, list, N * sizeof*list);
        cmp_count = insertion_sort(sorted, N);
        printf("Insertion sort: %d comparisons\n", cmp_count);
        // print_list(sorted, N);

        memcpy(sorted, list, N * sizeof*list);
        cmp_count = bubble_sort(sorted, N);
        printf("Bubble sort: %d comparisons\n", cmp_count);
        // print_list(sorted, N);

        memcpy(sorted, list, N * sizeof*list);
        cmp_count = 0;
        quicksort(sorted, N, &cmp_count);
        printf("Quicksort: %d comparisons\n", cmp_count);
        // print_list(sorted, N);

        memcpy(sorted, list, N * sizeof*list);
        cmp_count = 0;
        merge_sort(sorted, 0, N-1, &cmp_count);
        printf("Merge sort: %d comparisons\n", cmp_count);
        // print_list(sorted, N);

        // print_list(list, N);
        return 0;
    }
}