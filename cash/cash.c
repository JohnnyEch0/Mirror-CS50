#include <stdio.h>
#include <cs50.h>

int coins_needed(change);


int main(void)
{
    int input;
    do
    {
        input = get_int("How much change? (int>0)");
    }
    while (input < 1);
    // printf("%i\n", input);
    int output = coins_needed(input);
    print("%i coins needed", output);


}

int coins_needed(change)
{
    int counter = 0

    do
    {
        if change >= 25
        {
        change - 25;
        counter++;
        }
        else if change >= 10
        {
            change - 10;
            counter++;
        }
        else if change >= 5;
        {
            change - 5;
            counter++;
        }
        else if change >= 1;
        {
            change - 1;
            counter++;
        }
        else
            printf("Change calc error")
    }
    while (change > 0);
    return counter;

}
