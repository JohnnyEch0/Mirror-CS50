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
    // print a number of spaces before the #, so that they are centered
    for (int k = user_input - length_i; k > 0; k--)
    {
        printf(" ");
    }

    //print the first #'s
    for (int j = 0; j < length_i; j++)
        {

            printf("#");

        }

    // print the space in between
    printf("  ");

    //print the second #`s
    for (int j = 0; j < length_i; j++)
        {

            printf("#");

        }
    printf("\n");
}

