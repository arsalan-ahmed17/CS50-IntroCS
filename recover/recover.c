#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


typedef uint8_t BYTE;

const BYTE JPEG_HEADER[4] = { 0xff, 0xd8, 0xff, 0xe0 };

// Function to check if a given block matches the JPEG header
int is_jpeg_start(BYTE buffer[512])
{
    return (buffer[0] == JPEG_HEADER[0] && buffer[1] == JPEG_HEADER[1] &&
            buffer[2] == JPEG_HEADER[2] && (buffer[3] & 0xf0) == 0xe0); // 0xe0 to 0xef
}

int main(int argc, string argv[])
{
    // Ensure the program is executed with exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // Open the forensic image using CS50's get_string for interactive input
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Could not open file %s\n", argv[1]);
        return 1;
    }

    BYTE buffer[512];

    int file_count = 0;

    FILE *outfile = NULL;

    while (fread(buffer, sizeof(BYTE), 512, infile) == 512)
    {
        // Check if the current block is the start of a JPEG
        if (is_jpeg_start(buffer))
        {
            if (outfile != NULL)
            {
                fclose(outfile);
            }

            char filename[8];
            sprintf(filename, "%03d.jpg", file_count);
            outfile = fopen(filename, "w");
            if (outfile == NULL)
            {
                printf("Could not create output file %s\n", filename);
                fclose(infile);
                return 1;
            }

            file_count++;
        }

        if (outfile != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, outfile);
        }
    }

    if (outfile != NULL)
    {
        fclose(outfile);
    }

    fclose(infile);

    printf("Recovered %d JPEGs.\n", file_count);

    return 0;
}
