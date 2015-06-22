#include <stdio.h>
#include <stdlib.h>
#include "singly-linked-list.h"

// create a new list
list *mklist() {
    list *l = (list *)malloc(sizeof(list));
    l->head = NULL;
    l->tail = NULL;
    l->n = 0;
    return l;
}

// transverse
void transverse(list *l) {
    node *p = l->head;
    while (p != NULL) {
        printf("%d -> ", p->data);
        p = p->next;
    }
    printf("NULL\n");
}

// stack
void stack_push(list *l, int new_data) {
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = new_data;
    new_node->next = NULL;
    if (l->n == 0) {
        l->head = l->tail = new_node;
        l->n++;
    } else {
        new_node->next = l->head;
        l->head = new_node;
        l->n++;
    }
}

// stack
int stack_pop(list *l) {
    if (l->n == 0) {
        return -1;
    } else if (l->n == 1) {
        node *p = l->head;
        int data = p->data;
        l->head = l->tail = NULL;
        l->n--;
        free(p);
        return data;
    } else {
        node *p = l->head;
        int data = p->data;
        l->head = l->head->next;
        l->n--;
        free(p);
        return data;
    }
}

// queue
void queue_add(list *l, int new_data) {
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = new_data;
    new_node->next = NULL;
    if (l->n == 0) {
        l->head = l->tail = new_node;
        l->n++;
    } else {
        l->tail->next = new_node;
        l->n++;
    }
}

// queue
int queue_remove(list *l) {
    if (l->n == 0) {
        return -1;
    } else if (l->n == 1) {
        node *p = l->head;
        int data = p->data;
        l->head = l->tail = NULL;
        l->n--;
        free(p);
        return data;
    } else {
        node *p = l->head;
        int data = p->data;
        l->head = l->head->next;
        l->n--;
        free(p);
        return data;
    }
}

// insert new_data at location i
void list_insert(list *l, int i, int new_data) {
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = new_data;
    new_node->next = NULL;

    // consider spacial cases
    // new_node has no previous node
    if (i == 0) {
        l->head = l->tail = new_node;
        l->n++;
    } else {
        node *p = l->head;
        int k = 0;
        while (k < i - 1) {
            p = p->next;
            k++;
        } // k = i - 1
        new_node->next = p->next;
        p->next = new_node;
        l->n++;
    }
}

// delete node i
int list_delete(list *l, int i) {
    // consider when node i have no previous node
    if (i == 0) {
        node *p = l->head;
        int data = p->data;
        l->head = l->head->next;
        free(p);
        return data;
    } else {
        node *p = l->head;
        int k = 0;
        while (k < i - 1) {
            p = p->next;
            k++;
        } // k = i - 1
        node *nodei = p->next;
        int data = nodei->data;
        p->next = p->next->next;
        free(nodei);
        return data;
    }
}
