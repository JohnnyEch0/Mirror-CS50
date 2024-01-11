#include <stdio.h>
#include <cs50.h>

// this prints basic Stairs :)

void print_row(int length);


int main(void)
{
    int height = get_int("Height: ");
    for (int i = 0; i < height; i++)
    {
        print_row(i + 1);


    }
}

void print_row(int length)
{
    for (int j = 0; j < length; j++)
        {

            printf("#");
        }
    printf("\n");
}
