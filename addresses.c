#include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     int *p = &n; // declaring a pointer (a variable that will store the address of a variable.)
//     printf("%p \n", *p);
// }



int main() {
    int arr[3] = {5, 15, 25};
    int *ptr = arr;
    ptr++;
    printf("%d\n", *ptr);
    return 0;
}
