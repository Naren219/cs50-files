#include <stdio.h>

int main(void) {
   int N;
   scanf("%d", &N);
   void printNos(int N) {
        if (N > 0) //The loop runs till N>1
        {
            printNos(N-1); //We keep on recursing till the end as we want to pritn from 1 to N
            printf("%d ", N); //When recursion is done then print N
        }
        return;
    }
}
