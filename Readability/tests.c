#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string text = get_string("Please give me the text to evaluate:");
    int spaces = 0;
    int punc_marks = 0;
    int txt_len = strlen(text);

    for (int i = 0, n = txt_len; i < n; i++)
    {
        int letter = text[i];

        if (letter == 32)
        {
            spaces++;
        }
        else if (letter <= 64)
        {
            punc_marks++;
        }
    }
    float non_letters = spaces+punc_marks;
    float av_word_len = (float)(txt_len-non_letters) / (spaces+1) * 100;

    printf("%f is the average words per 100 words (kindoff haha)\n", av_word_len);
    
}
