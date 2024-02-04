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
    uint8_t header[3]; //3.5?

    while (fread(&buffer, 1, 512, input) == 512)
    {
        printf("block found\n");
        // if the block starts with 0xff 0xd8 0xff 0xe0 (last zero might be different)
        // --> start a new file
        //

    }

    // close files
    fclose(input);

    return 0;
}
