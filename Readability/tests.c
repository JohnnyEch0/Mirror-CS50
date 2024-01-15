#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string text = get_string("Please give me the text to evaluate:");
    int spaces = 0;
    int txt_len = strlen(text);

    for (int i = 0, n = txt_len; i < n; i++)
    {
        int letter = text[i];

        if (letter == 32)
        {
            spaces++;
            // printf("there is a space as position %i\n", i);
            //should i just count the spaces? is the number of words always the number of spaces+1?
        }

    }

    float av_word_len = txt_len-spaces / (spaces+1);

    // printf("there are %i spaces in this text, which should tell me that it has %i words\n", spaces, spaces + 1);
    printf("%f is the average word length\n", av_word_len);
}
