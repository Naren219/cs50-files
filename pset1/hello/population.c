#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // TODO: Prompt for start size

        int n;
do
{
      n = get_int("Starting size: ");
}
    while (n < 9);

    // TODO: Prompt for end size


        int i;
do
{
      i = get_int("End size: ");
}
    while (i < n);


    // TODO: Calculate number of years until we reach threshold

        int y = 0;
    while (n < i)
{
     n = round(n + n/3 - n/4);
      y++;
}

    // TODO: Print number of years
{

    printf("Years %i\n", y);
}

}