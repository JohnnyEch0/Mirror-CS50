// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // for 26*26 Hashtable
        // return ((toupper(word[0])-'A') * 26 + (toupper(word[1]) - 'A'))
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    printf("load reached");
    // TODO
    // open dict - check if return is NULL

    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // create a node
    // fscanf(file, "%s", word) --> word is an char array to save the word --> until fscanf returns EOF
    char *word_[LENGTH];


    while (fscanf(input, "%s", word_) != EOF)
    {

        // maloc *n -> check if return is NULL
        node *n = malloc(sizeof(node));
        if (n == NULL)
            return false;
        // copy the read word into the node

        strcpy(n->word, word_);
        //get the hash
        unsigned int x = hash(word_);
        // if there is nothing inside that linked list, have it point to new node
        printf("%p", table[x]->next);
        if (table[x]->next == NULL)
        {
            n->next = NULL;
            table[x]->next = n;

        }
        // else: new node points to first element of linked list, which points to new element
        else
        {
            n->next = table[x]->next;
            table[x]->next = n;
        }
        printf("%s", word_);

    }


    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
