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

    while (fread(&buffer, sizeof(buffer), 1, input) != 0)

}
