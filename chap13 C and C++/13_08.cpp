/*

Write a smart pointer class. A smart pointer is a data type, usually
implemented with templates, that simulates a pointer while also
providing automatic garbage collection. It automatically counts the
number of references to a SmartPointer<T*> object and frees the object
of type T when the reference count hits zero.

? how to automatically count references?

By overriding the equal operator.

Kind of like ARC(Automated References Counting) technology in
objective-c.

*/



#include <cassert>

template <typename T> class SmartPointer {
public:
    T *ptr;
    int *cnt;

    // Constructor from raw pointer
    SmartPointer(T *iptr) {
        ptr = iptr;
        cnt = new int;
        (*cnt) = 1;
    }

    // Constructor from SmarterPointer
    SmartPointer(SmartPointer<T> &sptr) {
        ptr = sptr.ptr;
        cnt = sptr.cnt;
        (*cnt)++;
    }

    // Override equal operator, increase counter by 1 when using = to
    // assign to variable
    SmartPointer<T> &operator=(SmartPointer<T> &sptr) {
        if (this == &sptr)
            return *this;

        if ((*cnt) > 0) {
            decrease();
        }

        ptr = sptr.ptr;
        cnt = sptr.cnt;
        (*cnt)++;
        return *this;
    }

    T getValue() {
        return *ptr;
    }

    // Destructor
    ~SmartPointer() {
        decrease(); // decrease counter
    }

    // decrease counter
    void decrease() {
        (*cnt)--;
        if ((*cnt) == 0) {
            delete ptr;
            delete cnt;
            ptr = NULL;
            cnt = NULL;
        }
    }
};


int main() {
    int *value = new int (7);

    // instantiate using raw pointer
    SmartPointer<int> sptr (value);
    assert(sptr.getValue() == *value);
    assert(*sptr.cnt == 1);


    // instantiate using SmartPointer reference
    SmartPointer<int> sptr2 (sptr);
    assert(sptr.getValue() == *value);
    assert(*sptr.cnt == 2);

    {
        // assign using equal operator
        int* dumpvalue = new int (0);
        SmartPointer<int> sptr3 (dumpvalue);
        sptr3 = sptr;
        assert(sptr.getValue() == *value);
        assert(*sptr.cnt == 3);
    } // sptr3 will be automatically destructed here

    assert(*sptr.cnt == 2);

    return 0;
}

// Local Variables:
// compile-command: "c++ 13_08.cpp -o 13_08 && ./13_08"
// End:
