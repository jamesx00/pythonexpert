class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age



alfie = Person("Alfie", 10)
leon = Student("Leon", 9, 4)