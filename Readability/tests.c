#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int main(void)
{
    string text = get_string("Please give me the text to evaluate:");
    int spaces = 0;
    int non_let_spa = 0; // was punc_marks
    int txt_len = strlen(text);
    int punc = 0; //was non_punc

    for (int i = 0, n = txt_len; i < n; i++)
    {
        int letter = text[i];

        if (letter == 32)
        {
            spaces++;
        }
        else if (letter <= 64)
        {
            // we need to check if the char is ?,! or .
            non_let_spa++;
            if (letter == 21 || letter == )
            {
                punc++; //was non_punc
            }
        }
    }

    float non_letters = spaces+non_let_spa;
    int word_count = spaces+1;
    // int punc = non_let_spa - non_punc; //was non_punc


    float av_word_len = (float)(txt_len-non_letters) / word_count * 100;
    float sen_p_words = (float)punc / word_count * 100;

    // printf("%f is the average words per 100 words (kindoff haha)\n", av_word_len);
    // printf("there are %f sentences per 100 words", sen_p_words);

    int index = round(0.0588 * av_word_len - 0.296 * sen_p_words - 15.8);

    printf("Level: %i\n", index);

}
