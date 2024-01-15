#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

void validate_input(string key);

int main(int argc, string argv[])
{
    if (argc == 1)
    {
        validate_input(argv[1]);
    }
    else
        printf("Usage: .substitution key");

}

void validate_input(string key)
{
    int len = strlen(key);
    if (len == 26)
    {
        printf("len verified");
    }
    else
        printf("input must be 26 letters");
}
