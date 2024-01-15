#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

void validate_input(string key);
bool has_letters(string key_l);

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
        bool let_check = has_letters(key);
    }
    else
        printf("input must be 26 letters\n");
}

bool has_letters(string key_l)
{
    for (int i=0; i < 26; i++);
    {
        bool test = strchr(key_l, ((int)'a' + i));
        if test == NULL
            return false;
    }
    return true;
}
