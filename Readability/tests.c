#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string text = get_string("Please give me the text to evaluate:");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (int(text[i]) == 32)
        {
            printf("there is a space as position %i", i)
        }
    }
}
