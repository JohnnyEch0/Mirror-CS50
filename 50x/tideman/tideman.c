#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
void swap(pair swap_set[1], pair swapset[2]);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);
        // printf(")

        // printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (!strcmp(name, candidates[i])) // if equal we get 0 - True
        {
            ranks[rank] = i;
            // printf("%s is at rank %i\n", candidates[i], rank);
            return true;
        }
    //
    }

    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count-1; i++)
    {
        for (int j = 0; j < candidate_count-1 -i; j++)
        {
            preferences[ranks[i]][ranks[j+1+i]]++;
            printf("%i points %s over %s\n",   preferences[ranks[i]][ranks[j+1+i]],  candidates[ranks[i]], candidates[ranks[j+i+1]]);
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    // read preferences
    // pairs is a list of pair that consist of int winner and int looser

    // for every candidate[i], when preferences[i][j] is > then [j][i] create pair candidate[i] candidate[j]

    // for every candidate[i]
    int pair_nr = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        //loop through every other candidate
        for (int j = 0; j < candidate_count-1 -i; j++)
        {
            //check wether pref[i][j+1+i] > then its counterpart
            if (preferences[i][j+i+1] > preferences[i+j+1][i])
            {
                pairs[pair_nr].winner = i;
                pairs[pair_nr].loser = j+i+1;
                pair_nr++;
                pair_count++;
                //printf("%s is the winner over %s by %i pints\n",  candidates[i],  candidates[i+j+1], preferences[i][j+i+1] - preferences[i+j+1][i] );
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    // theres a number of pairs, who win by different     amounts     =preferences[pairs[pair_nr].winner][pairs[pair_nr].loser]
    for (int i = 0; i < pair_count; i++)
    {
        // pairs[0], pairs[1] are i
        // preferences[pairs[i].winner][pairs[i].loser] = its points
        int i_value = preferences[pairs[i].winner][pairs[i].loser];
        pair low_pair;
        int low_pair_pos;
        bool swapped = false;

        for (int j = 0; j < pair_count; j++)
        {
            //compare it with the other pairs, pairs[j]
            int j_value = preferences[pairs[j].winner][pairs[j].loser];
            int j2_value = preferences[pairs[j+1].winner][pairs[j+1].loser];
            


            if (j_value < j2_value)
            {
                swap(&pairs[j], &pairs[j+1]);
                swapped = true;
            }
        }
        if (swapped == false)
        {
            for (int k = 0; k < pair_count; k++)
            {
                printf("%s wins over %s with %i points \n", candidates[pairs[k].winner], candidates[pairs[k].loser], preferences[pairs[k].winner][pairs[k].loser]);
            }
            break;
        }


        //Low_pair_pos might not even be set here, if no low value was ever found

    }

    // debug print stuffff

    return;
}

void swap(pair swap_set[1], pair swapset[2])
{
    pair temp = swap_set[1];
    swap_set[1] = swap_set[2];
    swap_set[2] = temp;

}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    return;
}
