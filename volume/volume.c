#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "rb"); // "rb" for reading binary
    if (input == NULL)
    {
        printf("Could not open input file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "wb"); // "wb" for writing binary
    if (output == NULL)
    {
        printf("Could not open output file.\n");
        fclose(input);
        return 1;
    }

    float factor = atof(argv[3]); // Volume scaling factor

    // Copy the header from input file to output file
    unsigned char header[HEADER_SIZE];
    fread(header, sizeof(unsigned char), HEADER_SIZE, input);
    fwrite(header, sizeof(unsigned char), HEADER_SIZE, output);

    // Read samples from input file and write adjusted samples to output file
    int16_t sample;
    while (fread(&sample, sizeof(int16_t), 1, input) == 1) // Read 16-bit sample
    {
        sample = (int16_t) (sample * factor);        // Adjust the volume (scale the sample)
        fwrite(&sample, sizeof(int16_t), 1, output); // Write the adjusted sample to output file
    }

    fclose(input);
    fclose(output);

    printf("Volume adjusted successfully!\n");
    return 0;
}
