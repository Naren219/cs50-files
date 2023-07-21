#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    //get an amount of change owed
    float change;
    do
    {
    change = get_float("Change owed: ");
    } while (change < 0);
    
    //setting values for different types of coins
    float quarter = 0.25;
    float dime = 0.10;
    float nickel = 0.05;
    float penny = 0.01;

    //check to see if divisible by any quarters:)
    float b;
    float c;
    float a;
    
    if (change / quarter > 1)
    {
         a = change / quarter;
    }
     //then dimes
         
         if (a / dime > 1)
        {
             b = a / dime;
        }

        //then check for nickels or else penny.

         if (b / nickel > 1)
        {
            c = b / nickel;
        }
        float d;
        
        else
        {
            d = c / penny;
        }
        printf("%i\n", d);
}
