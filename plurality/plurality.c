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
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election

    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // string name_check = candidate[i].name;
        if (!strcmp(name, candidates[i].name))
        {
            candidates[i].votes++;
            printf("%s  has %i votes\n", candidates[i].name, candidates[i].votes);
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    // Find out who has the most votes - by ordering everbody and printing the first
    candidate winner = find_winner();
    printf("%s wins the election with %i Votes.\n", winner.name, winner.votes);


    return;
}

candidate find_winner(void)
{
    // order the candidates by their votes

    // ini a variable to compare each candidate against
    candidate highest_fn = candidates[0];

    // loop through candidates and replace highest_fn if a a value is higher
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > highest_fn.votes)
            highest_fn = candidates[i];
    }

    return highest_fn;


}
