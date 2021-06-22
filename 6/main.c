#include <stdio.h>
#include <stdlib.h>

struct node {
    int val;
    struct node *link;
};

typedef struct list {
    struct node *head;
    int length;
} list;


struct node* XOR(struct node *x, struct node *y){
    return (struct node*)((__intptr_t)x ^ (__intptr_t)y);
}

list* list_new(){
    list *l;
    l = 0;

    l = malloc(sizeof *l);
    if(!l){
        printf("Error allocating new list\n");
        exit(1);
    }


    l->head = 0;
   
    l->length = 0;

    return l;
}

void _list_free_(struct node*n, struct node *prev, struct node *free_me) {
    if(!n) {
        free(free_me);
        free(prev);
        return;
    }
        
    if(free_me)
        free(free_me);

    _list_free_(XOR(n->link, prev), n, prev);

}

list* list_free(list *l){

    _list_free_(l->head, 0, 0);


    free(l);
    l = 0;
    return l;
}



void list_add(list *l, int val) {
    
    struct node *previous;
    struct node *current;
    struct node *next;

    struct node *new_node;

    
    previous = 0;
    new_node = 0;
    current = 0;

    new_node = malloc(sizeof *new_node);
    if(!new_node){
        printf("Memory allocation for new node failed\n");
        exit(1);
    }

    new_node->val = val;
    new_node->link = 0;


    if(!l->head) {
        l->head = new_node;
        new_node->link = XOR(0, 0);
        l->length = 1;
        return;
    }

    if(!l->head->link){
        l->length++;
        previous = l->head;
        l->head->link = XOR(0, new_node);
        new_node->link = XOR(0, previous);
        return;
    }
    /** 
     * Start at head. Need this outside of loop or else we stop early.
     * 
    */

    current = l->head;
    previous = 0;
    next = 0;
    next = XOR(previous, current->link);

    while(next != 0){
        
        previous = current;
        current = next;
        next = XOR(previous, current->link);
        
    }


    
    current->link = XOR(current->link, new_node);
    
    new_node->link = XOR(current, 0);

    l->length++;

 

}


void list_print(list *l){
    struct node *current;
    struct node *previous;
    struct node *next;

    int i;
    current = 0;
    previous = 0;
    next = 0;

    i = 0;

    current = l->head;

    

    while(current != 0){
        printf("%d | %d\n", i, current->val);
        
        next = XOR(current->link, previous);
        previous = current;
        current = next;

        i++;
        if(i == l->length){
            return;
        }
    }

}



int main(){
    list *l = list_new();
    list_add(l, 1);
    list_add(l, 2);
    list_add(l, 3);
    list_add(l, 4);

    list_print(l);

    list_free(l);

    return 0;
}