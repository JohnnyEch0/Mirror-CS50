#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("What is your name? ");
    int age = get_int("How old r u ? ");
    int phone_number = get_long("What's your Phone Number? ");
    
    printf("Hello, %s\n", name);
}
