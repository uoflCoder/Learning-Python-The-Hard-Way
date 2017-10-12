#Exercise 42
## Animal is-a object
class Animal(object):
    pass

##Dog is an Animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has a name
        self.name = name

##Cat is an Animal
class Cat(Animal):

    def __init__(self,name):
        ##Cat has a name
        self.name = name

##Person is an object
class Person(object):

    def __init__(self, name):
        ##Person has a name
        self.name = name

        ##Person has a pet of some kind
        self.pet = None

##Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
