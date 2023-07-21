#include <math.h>
#include <stdlib.h>
#include <stdio.h>


int x = 212;

void convertNumberIntoArray(unsigned int number) {
    unsigned int length = (int)(log10((float)number)) + 1;
    char * arr = (char *) malloc(length * sizeof(char)), * curr = arr;
    do {
        *curr++ = number % 10;
        number /= 10;
    } while (number != 0);
    printf("%s\n", arr);
}

int main(void)
{
    convertNumberIntoArray(x);
}



