#include <stdio.h>
#include <stdlib.h>


void print_list(double list[], int N) {
    for (int i = 0; i < N; i++) {
        printf("%g, ", list[i]);
    }
    printf("\n");
}


double* read_array(char filename[]) {
    printf("%s\n", filename);
    FILE *fp;
    fp = fopen(filename, "r");
    if (fp != NULL) {
        printf("success\n");
        float x;
        while (fscanf(fp, "%g", &x) != EOF) {
            printf("%g\n", x);
        }
        // FIXME
        fclose(fp);
    }
}


void swap(double list[], int i, int j) {
    double tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
}


void bubble_sort(double list[], int N) {
    for (int i = N; 0 < i; i--) {
        // printf("%d\n", i);
        for (int j = 1; j < i; j++) {
            if (list[j-1] > list[j]) {
                swap(list, j-1, j);
            }
            // printf("--> %d %d\n", j-1, j);
        }
    }
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        return 84;
    } else {
        // FIXME
        // read_array(argv[1]);
        int N = 4;
        double list[] = {3.3, 5, 9.89, -6};
        print_list(list, N);
        bubble_sort(list, N);
        print_list(list, N);
        return 0;
    }
}