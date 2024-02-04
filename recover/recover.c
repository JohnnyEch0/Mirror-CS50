#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // check 4 correct Usage
    if (argc != 2)
    {
        printf("Usage: ./recover [image to be recovered]\n");
        return 1;
    }

    // Open file
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }

    // create the buffer
    uint8_t buffer[512];
    int count = -1;
    char *out = malloc(8);


    while (fread(&buffer, 1, 512, input) == 512)
    {
        // if a new file is found, create a new name
        if (buffer[0] == 0xFF && buffer[1] == 0xD8 && buffer[2] == 0xFF && buffer[3] >= 0xE0)
        {
            count++;
            sprintf(out, "%.3d.jpg", count);
            // printf("%s\n", out);
            FILE *output = fopen(out, "w");
            if (output == NULL)
                printf("NOTFOUND");
        }

    }

    // close files
    fclose(input);

    free(out);

    return 0;
}
