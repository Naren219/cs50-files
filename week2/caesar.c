#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

string encipher(int length, string pt[]);
int k;

int main(int argc, string argv[])
{
    
    if (k >= 0)
    {
        k = atoi(argv[1]);
    }

    else
    {
        printf("Usage: ./caesar key\n");
    }
    string pt = get_string("plaintext: ");
    
    printf("ciphertext: %s\n", encipher(k, ct[]));
}

string encipher(int length, string pt[])
{
    int n = strlen(pt);
    for (int i = 0; i < n; i++)
    {
        if (isupper(pt[i])
        {
            int ct[i] = ((pt[i] - 65) + k) % 26;
        }
        else 
        {
            int ct[i] = ((pt[i] - 97) + k) % 26;
        }
    }
    return (string) ct;
}

