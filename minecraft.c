#include <stdio.h>

float arcsin(float value){

     float old = value;
     float new = value + (0.5 * ((value * value * value)/3));
     float accurate = 0.00001;

     if ((new - old) < accurate){
        return new;
     }

     else{
        return arcsin(new);
     }
}


int function_arcsin(int sigdig, float value){

    value = arcsin(value);
    printf("%.10e\n",value);

    return 0;
}