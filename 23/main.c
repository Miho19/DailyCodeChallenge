#include <stdio.h>
#include <stdlib.h>

#include <string.h>


struct node {
    struct node *left;
    struct node *right;
    int value;
};

struct bst {
    struct node *root;
};

struct bst* bst_new(){
    struct bst *b = malloc(sizeof(*b));
    b->root = 0;
    return b;
}

void node_destroy(struct node *root){

    if(root->left)
        node_destroy(root->left);
    if(root->right)
        node_destroy(root->right);
    free(root);    
}

struct bst* bst_destroy(struct bst *b){
    node_destroy(b->root);
    free(b);
    b = 0;
    return b;
}

int node_add(struct node **curr, struct node **new_node){
    
    if(!*curr){
        *curr = *new_node;
        return 1;
    }

    if((*(curr))->value == (*(new_node))->value) {
        free((*(new_node)));
        return 0;
    }

    return (*(curr))->value > (*(new_node))->value ? node_add(&(*(curr))->left,new_node) : node_add(&(*(curr))->right,new_node);
}

int bst_add(struct bst *b, int item){
    struct node *new_node = malloc(sizeof(*new_node));
    new_node->left = 0;
    new_node->right = 0;
    new_node->value = item;

    if(!b->root) {
        b->root = new_node;
        return 0;
    }

    return node_add(&b->root, &new_node);
}


void print_int(int data){
    
    printf("%d\n", data);
}

void node_print(struct node *curr, void (*print_function)(int)){
    if(curr == 0)
        return;

    node_print(curr->left, print_function);

    print_function(curr->value);

    node_print(curr->right, print_function); 
    
}



void bst_print(struct bst *b, void (*print_function)(int)){
    node_print(b->root, print_function);
}

void node_dive(struct node *curr, int level, int *deepest, int *deep_value){
    if(curr) {
        level++;
        node_dive(curr->left, level, deepest, deep_value);

        if(level > *deepest){
            *deepest = level;
            *deep_value = curr->value;
        }

        node_dive(curr->right, level, deepest, deep_value);
    }
}

int bst_height(struct bst *b){
    int deepest_level = 0;
    int deep_value = 0;

    node_dive(b->root, 0, &deepest_level, &deep_value);

    return deep_value;
}


int main(void){
    
    struct bst *b = bst_new();
    
    bst_add(b, 10);
    bst_add(b, 6);
    bst_add(b, 7);
    bst_add(b, 5);

    bst_add(b, 20);
    bst_add(b, 15);
    bst_add(b, 21);
    
    bst_add(b, 4);
    bst_add(b, 14);
    bst_add(b, 16);
    bst_add(b, 33);
    bst_add(b, 13);



    bst_print(b, print_int);

    printf("deepest value: %d\n", bst_height(b));

    b = bst_destroy(b);
    return 0;
}