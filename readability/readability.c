#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// Declare functions to count letters, words, and sentences in the text
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user to input a block of text
    string text = get_string("Text: ");

    // Calculate the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Use the counts to compute the Coleman-Liau index
    float L = (float) letters / words * 100; // Average letters per 100 words
    float S = (float) sentences / words * 100; // Average sentences per 100 words
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Display the appropriate grade level based on the index
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index)); // Round index to the nearest whole number
    }
}

// Count how many alphabetic characters are in the given text
int count_letters(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            count++; // Increment the count for each letter found
        }
    }
    return count;
}

// Count how many words are in the given text
int count_words(string text)
{
    int count = 1; // Start at 1 since the last word doesn't end with a space
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]))
        {
            count++; // Increment the count for each space (indicating a new word)
        }
    }
    return count;
}

// Count how many sentences are in the given text
int count_sentences(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Look for sentence-ending punctuation: '.', '!', or '?'
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++; // Increment the count for each sentence-ending character
        }
    }
    return count;
}
