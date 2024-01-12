#include <stdio.h>
#include <cs50.h>

int coins_needed(int change);

int main(void)
{
    int input;
    do
    {
        input = get_int("Change owed:");
    }
    while (input < 1);
    // printf("%i\n", input);
    int output = coins_needed(input);
    printf("%i coins needed\n", output);
}

int coins_needed(change)
{
    int counter = 0;

    do
    {
        counter++;
        if (change >= 25)
        {
            change = change - 25;
        }
        else if (change >= 10)
        {
            change = change - 10;
        }
        else if (change >= 5)
        {
            change = change - 5;
        }
        else if (change >= 1)
        {
            change = change - 1;
        }
        else
            printf("Change calc error");
    }
    while (change > 0);
    return counter;
}
