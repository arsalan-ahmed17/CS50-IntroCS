#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Calculate how many quarters you should give customer
    int quarters = calculate_quarters(cents);

    // Subtract the value of those quarters from cents
    cents = cents - (quarters * 25);

    int dimes = calculate_dimes(cents);
    cents = cents - (dimes * 10); // Subtract the value of dimes

    int nickels = calculate_nickels(cents);
    cents = cents - (nickels * 5);

    int pennies = calculate_pennies(cents);
    cents = cents - (pennies * 1);

    int total_coins = quarters + dimes + nickels + pennies;

    // Print the results
    printf("Quarters: %d\n", quarters);
    printf("Dimes: %d\n", dimes);
    printf("Nickels: %d\n", nickels);
    printf("Pennies: %d\n", pennies);
    printf("TOTAL COINS: %d\n", total_coins);
}

// Calculate how many quarters you should give customer DEFINING CALCULATE_QUARTERS
int calculate_quarters(int cents)
{
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
// Calculate how many dimes you should give customer DEFINING CALCULATE_DIMES
int calculate_dimes(int cents)
{
    int dimes = 0;
    while (cents >= 10)
    {
        dimes++;
        cents -= 10;
    }
    return dimes;
}
// Calculate how many nickels you should give customer DEFINING CALCULATE_NICKELS
int calculate_nickels(int cents)
{
    int nickels = 0;
    while (cents >= 5)
    {
        nickels++;
        cents -= 5;
    }
    return nickels;
}
// Calculate how many pennies you should give customer DEFINING CALCULATE_PENNIES
int calculate_pennies(int cents)
{
    int pennies = 0;
    while (cents >= 1)
    {
        pennies++;
        cents -= 1;
    }
    return pennies;
}
