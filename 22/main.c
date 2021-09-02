#include <stdio.h>
#include <stdlib.h>

#include <string.h>

struct node {
    struct node *next;
    int data;
};


struct list {
    struct node *head;
    int length;
};

void* emalloc(size_t s){
    void *result = 0;

    result = malloc(s);
    if(!result){
        fprintf(stderr, "Error allocating memory for size: %ld\n", s);
        exit(1);
    }

    return result;
}

struct list* list_new(){
    struct list *l = 0;
    l = emalloc(sizeof(*l));
    l->head = 0;
    l->length = 0;
    return l;
}

struct list* list_destroy(struct list *l){
    struct node *curr = 0;
    struct node *temp = 0;
    curr = l->head;

    while(curr != 0){
        temp = curr->next;
        free(curr);
        curr = temp;
    }

    free(l);
    l = 0;
    return l;
}

void list_add(struct list *l, int item){
    struct node *curr = 0;
    struct node *new_node = 0;

    if(!l || !item)
        return;

    new_node = emalloc(sizeof(*new_node));
    new_node->data = item;
    new_node->next = 0;

    if(l->head == 0){
        l->head = new_node;
        l->length = 1;
        return;
    }

    curr = l->head;

    while(curr->next != 0)
        curr = curr->next;
        
    curr->next = new_node;
    l->length++;
}

void list_print(struct list *l){
    struct node *curr = l->head;

    while(curr != 0){
        printf("%d\n", curr->data);
        curr = curr->next;
    }
}

void list_reverse(struct list *l){
    struct node *curr = 0;
    struct node *nxt = 0;
    struct node *prev = 0;

    if(!l)
        return;
    
    curr = l->head;
    prev = 0;
    
    while(curr != 0){
        nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }

    l->head = prev;

}

int main(void){
    int i;
    struct list *l = list_new();
    
    for(i=1;i<10;i++)
        list_add(l, i);

    list_print(l);

    list_reverse(l);

    list_print(l);

    l = list_destroy(l);   
    return 0;
}