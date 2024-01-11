#include <stdio.h>
#include <cs50.h>

void print_row(int length_i, int user_input);


int main(void)
{
    int height;
    do
    {
        height = get_int("How big Should the Construct be? (Int1-8)");
    }
    while (1 > height || height > 8);


    for (int i = 0; i < height; i++)
    {
        print_row(i + 1, height);
    }
}

void print_row(int length_i, int user_input)
{
    for (int k = user_input - length_i; k > 0; k--)
    {
        printf(" ");
    }

    for (int j = 0; j < length_i; j++)
        {
            printf("#");
        }

    printf("  ");

    for (int j = 0; j < length_i; j++)
        {
            printf("#");
        }
    printf("\n");
}

