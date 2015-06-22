// define node type
struct node {
    int data;
    struct node *next;
};
typedef struct node node;

// define list type
typedef struct {
    node *head;
    node *tail;
    int n;
} list;

list *mklist();
void transverse(list *l);

void stack_push(list *l, int new_data);
int stack_pop(list *l);
void queue_add(list *l, int new_data);
int queue_remove(list *l);
void list_insert(list *l, int i, int new_data);
int list_delete(list *l, int i);
