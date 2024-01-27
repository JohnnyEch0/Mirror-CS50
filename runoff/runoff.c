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

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
            //print to get

            // the candidate at that rank
            // printf("%s ", candidates[preferences[i][j]].name );
            // prefered by
            // printf(" is pref of voter %i", i);
            // at rank
            // printf(" at rank %i \n", j);
        }
        // printf("\n");
    }


    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // check if everything works until here

        // for (int i = 0; i < candidate_count; i++)
        //     printf("%s has %i votes, \n", candidates[i].name, candidates[i].votes);





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

        //end the program

        printf("prog ended\n");
        return 0;

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
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (!strcmp(name, candidates[i].name)) // if equal we get 0 - True
        {
            // ranks[rank] = i;
            // printf("%s is at rank %i\n", candidates[i], rank);

            // i is the number of the candidate?
            preferences[voter][rank] = i;
            // printf("%i is  the rank, name:%s\n", rank, name);
            return true;
        }
    //
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
// temp variable for the highest resuolt

    candidate winner_1 =  candidates[0];

    // check if there is a winner
    for (int i = 0; i < candidate_count; i++)
    {
        if (winner_1.votes < candidates[i].votes)
        {
            winner_1 = candidates[i];
        }
    }
    // print if it works

    // printf("%s has %i votes\n", winner_1.name, winner_1.votes);


    // check if some1 has the same score
    for (int i = 0; i < candidate_count; i++)
    {
        if (winner_1.votes == candidates[i].votes && winner_1.name != candidates[i].name)
        {
            candidate winner_2 = candidates[i];

            // check print
            // printf("%s has %i votes aswell\n", winner_2.name, winner_2.votes);

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

    int lowest_votes = candidates[0].votes;

    // find the lowest amount of votes
    for (int i = 0; i < (candidate_count-1); i++)
    {
        if (candidates[i].votes > candidates[i+1].votes && !candidates[i].eliminated && !candidates[i+1].eliminated)
        {
            lowest_votes = candidates[i+1].votes;
        }
    }
    printf("%i is the lowest amount of votes \n", lowest_votes);
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
    printf("all cand have the same nr of votes");
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    return;
}
