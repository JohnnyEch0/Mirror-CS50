#include <stdio.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    // out: char *plates[8];
    // this is a string

    // in: char *plates[8][7];
    // we need a list of strings

    // pointer out.
    char plates[8][7];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Save plate number in array
        for (int i = 0; i < 7; i++)
            plates[idx][i] = buffer[i];

        idx++;
    }

    for (int i = 0; i < 8; i++)
    {
            printf("%s\n", plates[i]);
    }
}
