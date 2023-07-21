#include <stdio.h>
#include <cs50.h>
#include <math.h>


float average(int length, int array[]);

int main(void)
{
    int TOTAL = get_int("Total number of scores: ");

    int scores[TOTAL];
    for (int i = 0; i < TOTAL; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }

    printf("Average: %.1f\n", average(TOTAL, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) length;
}

