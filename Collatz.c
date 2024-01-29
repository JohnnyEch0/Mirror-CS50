#include <stdio.h>
#include <cs50.h>


void collatz(int x, int y)
{
    if (x == 1)
        printf("%i steps to Collatz %i", y, x);

    else if (argc % 2 == 0)
    {
        y++;
        return collatz(x/2, y);
    }

    else
    {
        y++;
        return collatz(3*x + 1, y);
    }

}


void main(int argc, string argv)
{
    if (argc != 2)
        return 1;


    collatz(argv[1], 0);
}
