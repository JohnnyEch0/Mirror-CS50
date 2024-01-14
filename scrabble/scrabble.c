#include <stdio.h>
#include <cs50.h>
#include <string.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    word1 = get_string("player1 word?");
    word2 = get_string("player2 word?");


    int value[0] = calc_points(word1);
    int value[1] = calc_points(word2);

}

int calc_points(string word)
{
    for (i=0, n=strleng(word); i < n; i++)
    {
        int points = 0;

        if (isupper(word[i]))
        {
            points += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            points += POINTS[word[i] - 'a'];
        }
    }
    return score
}

// for each player, check each letter of the word and assign it a value, add them together and compare them
