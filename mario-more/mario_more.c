#include <stdio.h>
#include <cs50.h>

void print_row(int length);

// this seems really clunky, kinda works for everything below 5, but not for things above 5, also print row is really ugly


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
    // print a number of spaces before the #, so that they are centered
    for (int k = 5 - length; k > 0; k--)
    {
        printf(" ");
    }

    //print the first #'s
    for (int j = 0; j < length; j++)
        {

            printf("#");

        }

    // print the space in between
    printf("  ");

    //print the second #`s
    for (int j = 0; j < length; j++)
        {

            printf("#");

        }
    printf("\n");
}
