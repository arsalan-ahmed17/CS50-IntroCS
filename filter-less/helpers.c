#include "helpers.h"
#include <math.h>
#include <cs50.h> 

// Converts an image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Calculate the average of the red, green, and blue values
            int avg = round((float)(red + green + blue) / 3);

            // Set the RGB values to the average if the pixel is not already gray
            if (red != green || green != blue)
            {
                image[i][j].rgbtRed = avg;
                image[i][j].rgbtGreen = avg;
                image[i][j].rgbtBlue = avg;
            }
        }
    }
}

// Converts an image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            // Apply the sepia filter formula
            int newRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int newGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int newBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            // Clamp values to be between 0 and 255
            if (newRed > 255) newRed = 255;
            if (newGreen > 255) newGreen = 255;
            if (newBlue > 255) newBlue = 255;

            // Set the new RGB values
            image[i][j].rgbtRed = newRed;
            image[i][j].rgbtGreen = newGreen;
            image[i][j].rgbtBlue = newBlue;
        }
    }
}

// Reflects an image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap the pixel with its mirror counterpart
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
}

// Blurs an image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of the image to store the blurred result
    RGBTRIPLE copy[height][width];

    // Iterate through each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redSum = 0, greenSum = 0, blueSum = 0;
            int count = 0;

            // Loop through the 3x3 grid of pixels surrounding the current pixel
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Check if the neighboring pixel is within bounds
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        redSum += image[ni][nj].rgbtRed;
                        greenSum += image[ni][nj].rgbtGreen;
                        blueSum += image[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            copy[i][j].rgbtRed = round((float)redSum / count);
            copy[i][j].rgbtGreen = round((float)greenSum / count);
            copy[i][j].rgbtBlue = round((float)blueSum / count);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
}
