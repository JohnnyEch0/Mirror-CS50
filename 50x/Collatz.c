#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>


void collatz(int x)
{
    if (x == 1)
        return 1;

    else if (x % 2 == 0)
        return 1 + collatz(x/2);

    else
        return 1 + collatz(3*x + 1);
}


int main()
{
    int x = get_int("Whats the numver to be Collatz'd?");
    int y = collatz(x);
    printf("%i steps to Collatz\n", y)
}
