#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>


void collatz(int x, int y)
{
    if (x == 1)
        printf("%i steps to Collatz %i", y, x);

    else if (x % 2 == 0)
    {
        y++;
        collatz(x/2, y);
    }

    else
    {
        y++;
        collatz(3*x + 1, y);
    }

}


int main(int argc, string argv[])
{
    // int x = (argv[1]);
    collatz(x, strtol(argv[1]));
}
