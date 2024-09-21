"""
@Miguel Angel Cabrera Victoria
miguelangelcabreravictoria@gmail.com

Factory Method Pattern 
"""
from abc import ABCMeta , abstractmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractmethod
    def person_method():
        """Interface Method"""
        
class Student(IPerson):
    
    def __init__(self):
        self.name = "Basic Student Name"
    
    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    
    def __init__(self):
        self.name = "Basic Teacher Name"
        
    def person_method(self):
        print("I am a Teacher")
        

class PersonFactory:
    
    @staticmethod
    def build_person(person_type):
        if person_type == "Student" or person_type == "student":
            return Student()
        if person_type == "Teacher" or person_type == "teacher":
            return Teacher()
        print("Invalid Type")
        return -1
        
        
if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()