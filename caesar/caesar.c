#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Function prototype
string caesar_cipher(string text, int key);

int main(int argc, string argv[])
{
    // Check for a valid command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if the key is numeric
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Key must be a non-negative integer.\n");
            return 1;
        }
    }

    // Convert the key from string to integer
    int key = atoi(argv[1]);

    // Get plaintext input from the user
    string plaintext = get_string("plaintext: ");

    // Encrypt the plaintext
    string ciphertext = caesar_cipher(plaintext, key);

    // Output the ciphertext
    printf("ciphertext: %s\n", ciphertext);
    return 0;
}

// Function to perform Caesar cipher encryption
string caesar_cipher(string text, int key)
{
    // Iterate over each character in the text
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            char base = isupper(text[i]) ? 'A' : 'a';
            text[i] = (text[i] - base + key) % 26 + base;
        }
    }
    return text;
}
