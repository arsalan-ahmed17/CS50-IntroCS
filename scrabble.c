#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Define how much each letter in Scrabble is worth
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Function to calculate the score of a word given by the user
int compute_score(string word)
{
    int score = 0;

    // Loop through each character of the given word
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // Convert the character to uppercase to ensure uniform scoring
        char c = toupper(word[i]);

        // Only process alphabetic characters
        if (isalpha(c))
        {
            // Adjust character value to match array indices (A=0, B=1, ..., Z=25)
            score += POINTS[c - 'A'];
        }
    }

    // Return the total score for the word
    return score;
}

int main(void)
{
    // Ask Player 1 to input their word
    string word1 = get_string("Player 1: ");

    // Ask Player 2 to input their word
    string word2 = get_string("Player 2: ");

    // Calculate the scores for the words provided by both players
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Compare scores and declare the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0; // Program ends successfully
}
