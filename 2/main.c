#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <assert.h>



#define LENGTH(x) (sizeof(x) / sizeof(x[0]))


int* product(int *arr, unsigned int n) {

    int *list;
    unsigned int i;
    unsigned int p;


    list = 0;
    p = 1;
    list = malloc(n * sizeof(int));

    if(!list)
        return 0;

    for(i=0;i<n;i++){
        p *= arr[i];
    }

    if(p == 0){
        memset(list, 0, n *sizeof(int));
        return list;
    }

    for(i=0;i<n;i++){
        list[i] = (p / arr[i]);
    }


    return list;
}


int main(){
    
    int* l;
    

    int l1[] = {1, 2, 3, 4, 5};
    int l1p[] = {120, 60, 40, 30, 24};

    int l2[] = {3, 2, 1};
    int l2p[] = {2, 3, 6};

    int l3[] = {7, 8, 9, 10, 11, 12, 0, 123 , 44, 5, 0};
    int l3p[] = {0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0};
    
    l = 0;
    l = product(l1, LENGTH(l1));
    assert(!memcmp(l, l1p, LENGTH(l1)));
    free(l);

    l = 0;
    l = product(l2, LENGTH(l2));
    assert(!memcmp(l, l2p, LENGTH(l2)));
    free(l);


    l = 0;
    l = product(l3, LENGTH(l3));
    assert(!memcmp(l, l3p, LENGTH(l3)));
    free(l);


    return 0;
}