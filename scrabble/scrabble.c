#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int calc_points(string word);

int main(void)
{
    string word1 = get_string("player1 word?\n");
    string word2 = get_string("player2 word?\n");

    int value[2];
    value[0] = calc_points(word1);
    value[1] = calc_points(word2);

    if (value[0] < value[1])
    {
        printf("player 2 wins %i points\n", value[1]);
    }
    else if (value[0] > value[1])
    {
        printf("player 1 wins with %i points\n", value[0]);
    }
    else
    {
        printf("Its a Tie.\n");
    }
}

int calc_points(string word)
{
    int points = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (isupper(word[i]))
        {
            points += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            points += POINTS[word[i] - 'a'];
        }
    }
    return points;
}
