#include <cs50.h>
#include<stdio.h>
#include <ctype.h>
#include <string.h>


bool validate_input(string key);
bool has_letters(string key_l);
string strupr(string key_u);


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        bool input_valid = validate_input(argv[1]);
        if (input_valid)
        {
            printf("insert a function here if all ok");
        }
        else
            return 1;
        // inster cyphering function here, return 0
    }
    else
    {
        printf("Usage: .substitution key\n");
        return 1;
    }

    string message = get_string("What's the message to be encrypted?\n");
    string cypher = message;
    for (int i = 0; i < strlen(message); i++)
        {
            if (isupper(message[i]))
            {
                int cyp_pos = (int)(message[i]) - 65;
                // printf("%c", argv[1][cyp_pos]);
                cypher[i] = toupper(argv[1][cyp_pos]);
            }
            else if (islower(message[i]))
            {
                int cyp_pos = (int)(message[i]) - 97;
                cypher[i] = tolower(argv[1][cyp_pos]);
            }
            else
            {
                printf("No Support for numb3rs or signs, sorry \n");
                return 1;
            }

        }
        printf("%s\n", cypher);
}

bool validate_input(string key)
{
    int len = strlen(key);
    if (len == 26)
    {
        printf("len verified\n");

        string key_up = strupr(key);

        bool let_check = has_letters(key_up);
        printf("has all letters is %s\n", let_check ? "true" : "false");
        return true;
    }
    else
    {
        printf("input must be 26 letters\n");
        return false;
    }
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
