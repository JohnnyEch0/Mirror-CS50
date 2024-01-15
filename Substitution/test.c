#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

void validate_input(string key);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        validate_input(argv[1]);
    }
    else
        printf("Usage: .substitution key\n");
    string abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


}

void validate_input(string key)
{
    int len = strlen(key);
    if (len == 26)
    {
        printf("len verified\n");
        bool has_letters(key);
    }
    else
        printf("input must be 26 letters\n");
}

bool has_letters(key_l)
{
    for (i=0; i < 26; i++);
    {
        strchr(key_l, (int)'a' + i)
    }
}
