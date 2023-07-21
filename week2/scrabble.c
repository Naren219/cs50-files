#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
typedef struct
    {
        string name;
        string score;
    }
    winner;

int compute_score(string word);

int main(int argc, string argv[])
{
    if (isdigit(arv[1]))
    {
        players = atoi(argv[1]);
    }
    else
    {
        printf("Usage: ./scrabble number of players\n");
    }
    // Get input words from both players
    winner num[players];

    for (i = 0; i < players; i++)
    {
        num[i].name = get_string("Player %i: ", i + 1);
    }


    // Score both words
    int score[players] = compute_score(num[i]);

    for (j = 1, int n = strlen(total[]); j < n; j++)
    {
        for (i = 0, int n = strlen(total[]); i < n; i++)
        {
            if (total[i] < total[j])
            
        }

    }
}
// Compute and return score for string

int compute_score(string word)
{
    int sum_points = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (isalpha(word[i]))
        {
            int letter_offset = toupper(word[i]) - 'A';
            sum_points += POINTS[letter_offset];
            total[i] = sum_points[i]
        }
    }
    return sum_points;
}
