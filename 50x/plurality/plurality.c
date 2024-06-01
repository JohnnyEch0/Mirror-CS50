#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);
candidate find_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

    // Initialize the Array of Candidates with argv
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    // get votes and check validity
    int voter_count = get_int("Number of voters: ");

    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");
        if (!vote(name)) // while testing, this also increases candidates[i].votes if True
        {
            printf("Invalid vote.\n");
        }
    }
    print_winner();
}

bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (!strcmp(name, candidates[i].name))
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    candidate winner = find_winner();         // this measures the highest nr of votes
    for (int i = 0; i < candidate_count; i++) // now print everybody w that number
    {
        if (candidates[i].votes == winner.votes)
            printf("%s\n", candidates[i].name);
    }
}

candidate find_winner(void)
{
    candidate highest_fn = candidates[0];
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > highest_fn.votes)
            highest_fn = candidates[i];
    }
    return highest_fn;
}
