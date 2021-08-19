#include <stdio.h>
#include <stdlib.h>

/** 
 * https://en.wikipedia.org/wiki/Exponentiation_by_squaring
 * word for word copy of this. 
 * Learnt a new algorithm today!
 * 
*/

int expon(int base, int exponent){
    int y = 1;
    if(exponent == 0)
        return 1;

    if(exponent < 0){
        base  = 1 / base;
        exponent *= -1;
    }
    
    while(exponent > 1){
        if(exponent % 2 == 0){
            base = base * base;
            exponent = exponent / 2;
        } else {
            y = base * y;
            base = base * base;
            exponent = (exponent - 1) / 2;
        }
    }

    return base * y;

}


int main(int argc, char **argv){
    
    
    int base = 0;
    int exponent = 0;

    if(argc < 3){
        printf("usage: ./main <base> <exponent>\n");
        return 0;
    }

    base        = atoi(argv[1]);
    exponent    = atoi(argv[2]);

    printf("%d^%d = %d\n", base, exponent, expon(base, exponent));

    return 0;

}