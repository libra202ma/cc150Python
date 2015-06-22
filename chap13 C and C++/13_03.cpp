/*

How do virtual functions work in C++?

Referenced answer:

A virtual function depends on a "vtable" or "Virtual Table". If any function of a class is declared to be virtual, a vtable is constructed which stores addresses of the virtual functions of this class. The compiler also adds a hidden vptr variable in all such classes which points to the vtable of that class. If a virtual function is not overridden in derived class, the vtable of the derived class stores the address of the function in its parent class. The vtable is used to resolve the address of the function when the virtual function is called. Dynamic binding in C++ is performed through the vtable methanism.

Thus, when we assign the derived class object to the base class pointer, the vptr variable points to the vtable of the derived class. This assignment ensures that the most derived virtual function gets called.

keyword: vtable/Virtual Table, vptr variabe, overriden

*/

using namespace std;

// Consider the following code
class Shape {
public:
    int edge_legnth;
    virtual int circumference() {
        cout << "Circumference of Base Class\n";
        return 0;
    }
};

class Triangle : public Shape {
public:
    int circumference() {
        cout << "Circumference of Triangle Class\n";
        return 3 * edge_legnth;
    }
};

void main() {
    Shape* x = new Shape();
    x->circumference(); // "Circumference of Base Class"
    Shape* y = new Triangle();
    y->circumference(); // "Circumference of Triangle Class"
}

/*

In the previous example, circumference is a virtual function in the Shape class, so it becomes virtual in each of the derived class (Triangle, etc). C++ non-virtual function calls are resolved at compile time with static binding, while virtual function calls are resolved at runtime with dynamic binding.

 */
