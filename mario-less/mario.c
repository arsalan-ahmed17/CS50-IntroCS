#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;

    do
    {
        n = get_int("Height of the pyramid?: ");
    }
    while (n < 1 || n > 8);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < n - i; j++)
        {
            printf(" ");
        }

        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
