#include <stdio.h>
#include <stdlib.h>
#include "doubly-linked-list.h"

// make a doubly linked list
// use a dummy to reduce edge cases
list *mklist() {
    list *l = (list *)malloc(sizeof(list));
    l->n = 1;
    node *dummy = (node *)malloc(sizeof(node));
    dummy->data = 0;
    dummy->prev = dummy;
    dummy->next = dummy;
    l->dummy = dummy;
    return l;
}

// return i-th node pointer
// o-th is node dummy
node *idx(list *l, int i) {
    if (i < l->n/2) {
        node *p = l->dummy;
        int k = 0;
        while (k < i) {
            p = p->next;
            k++;
        } // k = i
        return p;
    } else {
        node *p = l->dummy;
        int k = l->n;
        while (k > i) {
            p = p->prev;
            k--;
        } // k = i
        return p;
    }
}

// get data of i-th node
// i >= 1
int get(list *l, int i) {
    return idx(l, i)->data;
}

// set data of i-th node
// i >= 1
void set(list *l, int i, int data) {
    idx(l, i)->data = data;
}

// insert new node at i-th location
// i >= 1 since 0-th node is dummy
void insert(list *l, int i, int data) {
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = data;

    node *p = idx(l, i);
    new_node->next = p;
    new_node->prev = p->prev;
    p->prev->next = new_node;
    p->prev = new_node;

    l->n++;
}

// delete i-th node
int delete(list *l, int i) {
    node *p = idx(l, i);
    int data = p->data;
    p->prev->next = p->next;
    p->next->prev = p->prev;
    free(p);
    l->n--;
    return data;
}
