#include <math.h>
#include <stdlib.h>
#include <stdio.h>
//#include "array_file.h"

char *words[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"};
char *base10[] = {"hundred", "thousand", "million"};
int number_int;
char *number_string;

int main(void)
{
    printf("Type number: ");
    scanf("%i", &number_int);
    char *itoa(number_int, number_string, 2);

    for (int i = 0; i < 9; i++) {
        atoi(words)
    }
}

