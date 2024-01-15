#include <cs50.h>
#include<stdio.h>
#include <ctype.h>
#include <string.h>


void validate_input(string key);
bool has_letters(string key_l);
string strupr(string key_u);


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        validate_input(argv[1]);
    }
    else
        printf("Usage: .substitution key\n");

    string message = get_string("What's the message to be encrypted?\n");
    for (int i = 0; i > strlen(message); i++)
        {
            string cypher = message;
            if (isupper(message[i]))
            {
                int cyp_pos = (int)(message[i]) - 65
                cypher[i] = 
            }
            printf("%s\n", cypher);
        }
}

void validate_input(string key)
{
    int len = strlen(key);
    if (len == 26)
    {
        printf("len verified\n");

        string key_up = strupr(key);

        bool let_check = has_letters(key_up);
        printf("has all letters is %s\n", let_check ? "true" : "false");
    }
    else
        printf("input must be 26 letters\n");
}

string strupr(string key_u)
{
    for (int i = 0; i < strlen(key_u); i++)
    {
        if islower(key_u[i])
            key_u[i] = toupper(key_u[i]);
    }
    return key_u;
}

bool has_letters(string key_l)
{
    for (int i=0; i < 26; i++)
    {
        char *test = strchr(key_l, (int)'A' + i);
        // printf("%c is the letter being checked for\n", (char)('A' + i));
        if (test == NULL)
            return false;
    }
    return true;
}
