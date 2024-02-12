// Implements a dictionary's functionality

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
    // TODO
    // open dict - check if return is NULL
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // fscanf(file, "%s", word) --> word is an char array to save the word --> until fscanf returns EOF
    char *word[LENGTH];
    while (fscanf(input, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        strcopy(n->word, "word");
        hash(word);
        
    }

        // create a node
            // maloc *n -> check if return is NULL
            // strcopy(n->word, "word")
            // n->next = NULL;
        // find n for table[n] / hash the word(?)
            // hash returns the bucket- or the index for the hashlist
            // set new node pointer to the first element in the linked list
                // now have the list pointer ponint to new node

        // if there is a node there
            // node->next = the node already there
            // what if there are multiple nodes?


    //return True
    return false;
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
