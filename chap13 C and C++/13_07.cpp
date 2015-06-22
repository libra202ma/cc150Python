/*

Write a method that takes a pointer to a Node structure as a parameter
and returns a complete copy of the passed in data structure. The Node
data structure contains two pointers to other Nodes.

*/

Node* copyStructure(Node *node) {
    if (node == NULL) {
        return NULL;
    }
    Node* newnode = new Node;
    newnode->data = node->data;
    newnode->ptr1 = copyStructure(node->ptr1);
    newnode->ptr2 = copyStructure(node->ptr2);
    return newnode;
}
