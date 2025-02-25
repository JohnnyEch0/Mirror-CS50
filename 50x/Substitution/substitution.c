#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool validate_input(string key);
bool has_letters(string key_l);
bool encrypt(string key_e);
string strupr(string key_u);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        bool input_valid = validate_input(argv[1]);
        if (input_valid)
        {
            bool input2_valid = encrypt(argv[1]);
            if (input2_valid)
                return 0;
            else
                return 1;
        }
        else
            return 1; // return 1 if something isnt valid. printing hadled by input_valid func
    }
    else
    {
        printf("Usage: .substitution key\n");
        return 1;
    }
}

bool validate_input(string key)
{
    int len = strlen(key);
    if (len == 26)
    {
        string key_up = strupr(key);

        bool let_check = has_letters(key_up);
        if (let_check)
            return true;
        else
            return false;
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
        if islower (key_u[i])
            key_u[i] = toupper(key_u[i]);
    }
    return key_u;
}

bool has_letters(string key_l)
{
    for (int i = 0; i < 26; i++)
    {
        char *test = strchr(key_l, (int) 'A' + i);
        if (test == NULL)
            return false;
    }
    return true;
}

bool encrypt(string key_e)
{
    string message = get_string("plaintext: ");
    string cypher = message;
    for (int i = 0; i < strlen(message); i++)
    {
        if (isupper(message[i]))
        {
            int cyp_pos = (int) (message[i]) - 65;
            cypher[i] = toupper(key_e[cyp_pos]);
        }
        else if (islower(message[i]))
        {
            int cyp_pos = (int) (message[i]) - 97;
            cypher[i] = tolower(key_e[cyp_pos]);
        }
        else
        {
            cypher[i] = message[i];
        }
    }
    printf("ciphertext: %s\n", cypher);
    return true;
}
