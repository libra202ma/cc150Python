#include <iostream>
using namespace std;

#define NAME_SIZE 50

class Person {
public:
    virtual void aboutMe() {
        cout << "I am a person.";
    }
};

class Student : public Person {
public:
    void aboutMe() {
        cout << "I am a student";
    }
};

int main() {
    Person p = Student();
    p.aboutMe();

    return 0;
}



// Local Variables:
// compile-command: "c++ inheritance.cpp -o inheritance && ./inheritance"
// End:
