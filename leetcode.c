#include <stdio.h>
#include <stdbool.h>

bool is_palindrome(int x);

int main(void)
{
    int x;
    printf("Enter a number ");
    scanf("%d", &x);

    if (x < 0 || (x % 10 == 0  &&  x != 0))
    {
        printf("False\n");

    }
    else {
        if (is_palindrome(x))
        {
            printf("True\n");
        }
    else {
        printf("False\n");

    }
    }
    return 0;
}

bool is_palindrome(int x)
{
    int reversed = 0;
    int original = x;

    while (x > 0)
    {
        int digit = x % 10;
        reversed = reversed * 10 + digit;

        x /= 10;

    }
    return original == reversed;
}
