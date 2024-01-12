#include <stdio.h>
#include <cs50.h>

int coins_needed(int change);
int check_coin_size (int change1);

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
        int coin_size = check_coin_size(change);
        change = change - coin_size;
    }
    while (change > 0);
    return counter;

    int check_coin_size (int change1)
    {
        int coin_size = 0;
        if (change1 >= 25)
            coin_size = 25;
        else if (change1 >= 10)
            coin_size = 10;
        else if (change1 >= 5)
            coin_size = 5;
        else
            coin_size = 1;
        return coin_size
    }
}
