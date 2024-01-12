#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int input;
    do
    {
        input = get_int("How much change? (int>0)");
    }
    while (input < 1);
    printf("%i\n", input);


}
