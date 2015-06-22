class Person:
    def __init__(self):
        self.id = 0
        self.name = ""

    def aboutMe(self):
        print "I am a person."


class Student(Person):
    def aboutMe(self):
        print "I am a student."
