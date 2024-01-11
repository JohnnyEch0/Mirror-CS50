#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <stdlib.h>

bool valid_check(int number);



int main(void)
{
    long input = get_long("Please give me your credit card number?");
    bool is_valid = valid_check(input);



}

bool valid_check(int number)
{
    int digit = number % 10;

    bool valid = false;
    int counter = 0;
    int sum = 0;

    int nDigits = floor(log10(labs(number))) + 1;
    // printf("%i\n", nDigits);

    for (int i = 0; i > 5; i++) //len(number)
    {
        if (counter == 0)
        {
            sum = sum + digit;
            counter++;
        }
        else if (counter == 1)
        {
            digit = digit * 2;
            sum = sum + digit;
            counter--;
        }
        else
        {
            printf("Counter Error >1");
        }

    }
    return valid;
}
