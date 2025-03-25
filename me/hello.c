#include <stdio.h> // Included the standard library

int main(void) // Main Function where the program actually begins (sort of green flag)
{
    string answer = get_string("What's your name? "); //Promt the user to enter their name and store their name in a variable called answer
    printf("hello, %s\n", answer); // Print a greeting message using the user's input with %s as a placeholder for answer variable
}
