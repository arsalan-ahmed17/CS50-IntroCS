#include <cs50.h>
#include <stdio.h>

bool check_amex(long card);
bool check_mastercard(long card);
bool check_visa(long card);
bool luhn_check(long card);

int main(void)
{
    long card;
    do{
        card = get_long("Credit Card Number: ");
    }
    while
        (card < 1000000000000 || card > 9999999999999999);

    // Additional check for card type
    if (check_amex(card))
    {
        printf("AMEX\n");
    }
    else if (check_mastercard(card))
    {
        printf("MASTERCARD\n");
    }
    else if (check_visa(card))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }

    // Validate the card number using the Luhn algorithm
    if (luhn_check(card))
    {
        printf("VALID\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

// Check if card is American Express (15 digits, starts with 34 or 37)
bool check_amex(long card)
{
    return (card >= 340000000000000 && card < 350000000000000) ||
           (card >= 370000000000000 && card < 380000000000000);
}

// Check if card is Mastercard (16 digits, starts with 51-55)
bool check_mastercard(long card)
{
    return (card >= 5100000000000000 && card < 5600000000000000);
}

// Check if card is Visa (13 or 16 digits, starts with 4)
bool check_visa(long card)
{
    return (card >= 4000000000000 && card < 5000000000000) || // 13 digits
           (card >= 4000000000000000 && card < 5000000000000000); // 16 digits
}

// Luhn algorithm to check the validity of the card number
bool luhn_check(long card)
{
    int sum = 0;
    int digit_count = 0;

    // Loop through each digit of the card number, starting from the rightmost one
    while (card > 0)
    {
        int digit = card % 10;
        card /= 10;

        // For every second digit from the right, double it
        if (digit_count % 2 == 1)
        {
            digit *= 2;
            if (digit > 9) // If doubling results in a number greater than 9, subtract 9
            {
                digit -= 9;
            }
        }

        sum += digit;
        digit_count++;
    }

    // The card is valid if the total sum is divisible by 10
    return sum % 10 == 0;
}
