typedef struct node {
    int data;
    struct node *prev;
    struct node *next;
} node;

typedef struct {
    int n;
    node *dummy;
} list;

list *mklist();
node *idx(list *l, int i);
int get(list *l, int i);
void set(list *l, int i, int data);
void insert(list *l, int i, int data);
int delete(list *l, int i);
