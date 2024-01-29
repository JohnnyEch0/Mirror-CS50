#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }
    }


    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }
        // Eliminate last-place candidates
        int min = find_min();

        bool tie = is_tie(min);


        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (!strcmp(name, candidates[i].name))
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // for every candidate
   for ( int i = 0; i < voter_count; i++)
   {
        //iterate over their votes
        for (int j = 0; j < candidate_count; j++)
        {
            // get their hightest vote, if its not eliminated
            if (candidates[preferences[i][j]].eliminated != true)
            {
                candidates[preferences[i][j]].votes += 1;
                // break the loop for this voter
                break;
            }
        }

   }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    candidate winner_1 =  candidates[0];

    // check if there is a winner
    for (int i = 0; i < candidate_count; i++)
    {
        if (winner_1.votes < candidates[i].votes)
        {
            winner_1 = candidates[i];
        }
    }

    // check if some1 has the same score
    for (int i = 0; i < candidate_count; i++)
    {
        if (winner_1.votes == candidates[i].votes && winner_1.name != candidates[i].name)
        {
            // is the next line necessary?
            // candidate winner_2 = candidates[i];
            return false;
        }
    }

    printf("%s\n", winner_1.name);
    return true;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // temp variable for the lowest candidate
        // there could be a bug here, when candidates[0] has been eliminated

    int lowest_votes = candidates[0].votes;

    // find the lowest amount of votes

    for (int i = 0; i < (candidate_count-1); i++)
    {
        if (candidates[i].votes > candidates[i+1].votes && !candidates[i].eliminated && !candidates[i+1].eliminated)
        {
            lowest_votes = candidates[i+1].votes;
        }
    }
    return lowest_votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    for (int i = 0; i < (candidate_count); i++)
    {
        if (!candidates[i].eliminated)
        {
            if (candidates[i].votes != min)
                return false;
        }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    for (int i = 0; i< candidate_count; i++)
    {
        if (candidates[i].votes == min)
            candidates[i].eliminated = true;
    }
    return;
}
