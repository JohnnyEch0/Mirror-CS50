#include <stdio.h>
#include <cs50.h>


int main(void)
{
    long input = get_long("Please give me your credit card number?");

    string test = len(input)
    printf("%s\n", test)


}

bool Valid_check(int number)
{
    int digit = number % 10;

    bool valid = false;
    int counter = 0;
    int sum = 0;

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
