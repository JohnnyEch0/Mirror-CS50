#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string text = getstring("Please give me the text to evaluate:");
    for (int i = 0, int n = getlen(text); i < n; i++)
    {
        if int(text[i]) == 32
        {
            printf("there is a space as position %i", i)
        }
    }
}
