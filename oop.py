# class and object
# OBJECT ORIENTED PROGRAMMING:
# class: blueprint of object
# we use class keyword
class Student:
    def __init__(self, name, age, unit, doa):
        self.name = name
        self.age = age
        self.unit = unit
        self.doa = doa

    def greetstudent(self):
        other = "!"
        print("Hello " + self.name + other)
# create object with initialised value


student1 = Student("Joseph", "14", "Form 1", "Thursday")
student2 = Student("Mary", "14", "Form 1", "Thursday")
print(student1.name)
student1.greetstudent()
student2.greetstudent()

# ENCAPSULATION: describe an idea of wrapping data in methods that will work on data within one unit


class subject:
    def __init__(self, name, student):
        self.name = name
        self.student = student

    def addedsubject(self):
        print("The subject " + self.name + " has been added to " + self.student.name)


mathsubject = subject("math", student2)
mathsubject.addedsubject()

# INHERITANCE: capability of a class to derive and inherit values from a different class
# two level of parties are involved: parent and child
# BENEFITS:
# reusability
# represents real world relationships
# transitive in nature


# single inheritance:mother child
# multi level inheritance:mother child grandchild
# hierarchial inheritannce:mother children
# multiple inheritance:mother father children
class Person(object):
    def __init__(self, name, staffnumber):
        self.name = name
        self.staffnumber = staffnumber
    def display(self):
        print(self.name)
        print(self.staffnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("My staffnumber is {}".format(self.staffnumber))


class Employee(Person):  # use commas to list more parents
    def __init__(self, name, staffnumber, salary, department):
        self.salary = salary
        self.department = department
        # call init function to parent
        Person.__init__(self, name, staffnumber)
# polymorphism: having many forms
# done by defining names but having different details

    def details(self):
        print("My name is {}".format(self.name))
        print("My staffnumber is {}".format(self.staffnumber))
        print("My salary is {}".format(self.salary))
        print("My department is {}".format(self.department))


a = Employee("Francis", 1234, 100000000, "software engineering")
# call methods from parent class
a.display()
a.details()
