// Implements a dictionary's functionality

#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 25;

// Hash table
node *table[N];

unsigned int size_dict;



// Returns true if word is in dictionary, else false
bool check(char *word)
{
    unsigned int index = hash(word);
    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
    {
        if (strcasecmp(cursor->word, word) == 0)
            return true;
        else
            continue;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(char *word_dict)
{
    return (tolower(word_dict[0]) - 97);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    char *word_dict;
    //char *word_table;
    FILE *file = fopen("dictionary", "r");
    if (file == NULL)
    {
        return false;
    }

        do {
            node *n = malloc(sizeof(node));
            if (n == NULL)
                return false;
            else
            {
                fscanf(file, "%s", word_dict);
                char *strcpy(node *n->word, const char* word_dict);
                //n->word = word_table;
                n->next = NULL;
                size_dict++;
                unsigned int index = hash(word_table);
                if (!table[index])
                {
                    table[index]->word = n->word;
                }
                else
                {
                    n->next = table[index]->word;
                    table[index]->word = n->word;
                }
             }

           } while (!feof(file));

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return size_dict;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        while(table->word)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
            return true;
        }
    }
    return false;
}
