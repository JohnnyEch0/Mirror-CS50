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
        return 1;
    }

    // create the buffer
    uint8_t buffer[512];
    int count = -1;
    char *out = malloc(8);
    FILE *output;


    while (fread(&buffer, 1, 512, input) == 512)
    {
        // if a new file is found, create a new name
        if (buffer[0] == 0xFF && buffer[1] == 0xD8 && buffer[2] == 0xFF && buffer[3] >= 0xE0)
        {
            if (output != NULL)
                fclose(output);
            count++;
            sprintf(out, "%.3d.jpg", count);
            // printf("%s\n", out);
            output = fopen(out, "w");

        }
        if (output != NULL)
            fwrite(&buffer, sizeof(buffer), 1, output);
    }

    // close files
    fclose(input);
    fclose(output);

    // free malloc
    free(out);

    return 0;
}
