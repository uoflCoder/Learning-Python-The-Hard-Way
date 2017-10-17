#Exercise 44
class Parent(object):

    def __init__(self, stuff):
        self.stuff = stuff + " Parent"
        print(self.stuff)

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def __init__(self, stuff):
        #inheritance
        self.stuff = stuff
        print(self.stuff)
        super(Child, self).__init__("Child")
        print(self.stuff)

        #composition
        self.other = Other()

    def implicit(self):
        #composition
        self.other.implicit()


    def override(self):
        print("CHILD override()")

    def altered(self):
        #Inheritance using super
        print("CHILD BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

        print("\n")
        print("CHILD BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

dad = Parent("Parent")
son = Child("Child")

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
