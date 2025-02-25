// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

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

const unsigned int N = 17550;

// Hash table
node *table[N];

unsigned int size_oflist(node *cursor)
{
    int count = 0;

    while (cursor != NULL)
    {
        count++;
        cursor = cursor->next;
    }
    return count;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int x = hash(word);
    node *cursor = table[x];
    if (cursor == NULL)
        return false;
    for (int i = 0, j = size_oflist(table[x]); i < j; i++)
    {
        if (!strcasecmp(cursor->word, word))
            return true;
        else if (cursor->next == NULL)
            return false;
        else
            cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // for 26*26 Hashtable
    // return ((toupper(word[0])-'A') * 26 + (toupper(word[1]) - 'A'))
    if (strlen(word) == 1)
        return (toupper(word[0]) - 'A') * 676;
    else if (strlen(word) == 2)
        return ((toupper(word[0]) - 'A') * 676 + (toupper(word[1]) - 'A') * 26);
    else
        return ((toupper(word[0]) - 'A') * 676 + (toupper(word[1]) - 'A') * 26 + (toupper(word[0]) - 'A'));
    // return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // open dict - check if return is NULL

    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // char *word_[LENGTH]; big mistaky
    char *word_ = malloc(LENGTH);

    // fscanf(file, "%s", word) --> word is an char array to save the word --> until fscanf returns EOF
    while (fscanf(input, "%s", word_) != EOF)
    {
        // create a node
        // maloc *n -> check if return is NULL
        node *n = malloc(sizeof(node));
        // TODO, Free Memory thus far if n == NULL
        if (n == NULL)
            return false;

        // copy the read word into the node
        strcpy(n->word, word_);

        // get the hash
        unsigned int x = hash(word_);
        // if there is nothing inside that linked list, have it point to new node

        // tablex[x]-> next - big mistakey
        if (table[x] == NULL)
        {
            n->next = NULL;
            table[x] = n;
        }
        // else: new node points to first element of linked list, which points to new element
        else
        {
            n->next = table[x];
            table[x] = n;
        }
    }
    free(word_);
    fclose(input);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    node *cursor;
    int count = 0;
    for (int i = 0; i < N; i++)
    {
        cursor = table[i];
        while (cursor != NULL)
        {
            count++;
            cursor = cursor->next;
        }
    }
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *cursor;
    node *tmp;
    for (int i = 0; i < N; i++)
    {
        cursor = table[i];
        while (cursor != NULL)
        {
            tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
