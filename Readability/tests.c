#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int calc_index(string input);
void print_answer(int p_index);


int main(void)
{
    string text = get_string("Please give me the text to evaluate:");
    int index = calc_index(text);
    print_answer(index);
}


int calc_index(string input)
{
    int spaces = 0;
    int non_let_spa = 0;
    int txt_len = strlen(input);
    int punc = 0;

    for (int i = 0, n = txt_len; i < n; i++)
    {
        int letter = input[i];

        if (letter == 32)
            spaces++;
        else if (letter <= 64) // we need to check if the char is ?,! or .
        {
            non_let_spa++;
            if (letter == 33 || letter == 63 || letter == 46)
                punc++;
        }
    }

    float non_letters = spaces+non_let_spa;
    int word_count = spaces+1;

    float av_word_len = (float)(txt_len-non_letters) / word_count * 100;
    float sen_p_words = (float)punc / word_count * 100;

    int index = round(0.0588 * av_word_len - 0.296 * sen_p_words - 15.8);
    return index;
}

void print_answer(int p_index)
{
    if (p_index < 1)
        printf("Before Grade 1\n");
    else if (p_index > 16)
        printf("Grade 16+\n");
    else
        printf("Grade %i\n", p_index);
}
