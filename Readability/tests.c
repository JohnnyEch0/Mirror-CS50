#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string text = get_string("Please give me the text to evaluate:");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        int letter = text[i];
        int spaces = 0;
        if (letter == 32)
        {
            spaces++;

            printf("there is a space as position %i\n", i);

            //should i just count the spaces? is the number of words always the number of spaces+1?
        }
        printf("there are %i spaces in this text, which should tell me that it has %i words", spaces, spaces + 1);
    }
}
