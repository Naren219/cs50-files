#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

    typedef struct
    {
        string name;
        string number;
    }
    person;

int main(int argc, string argv[]);
    {
        int count = int argc;
    }
{
    person people[count];
    for (int i = 0; i < count; i++)
    {
        string people[i].name = get_string("What are the names? ");
        string people[i].number = get_string("What are the numbers? ");
    }
        string finding = get_string("Which number do you want to find? ");

        void function()
    for (int i = 0; i < count; i++)
    {
        if (strcmp(finding, people[i].name) == 0)
        {
            printf("Found: %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not Found");
    return 1;
}