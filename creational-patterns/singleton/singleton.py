"""
@Miguel Angel Cabrera Victoria
miguelangelcabreravictoria@gmail.com

Singleton Pattern
"""

from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def print_data():
        """implement in child class"""

class PersonSingleton(IPerson):
    
    __instance = None
    
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton instance already exists")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
            
    @staticmethod
    def print_data():
        if PersonSingleton.__instance: 
            print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")
        else:
            print("No instance available")
    
    @staticmethod
    def delete_instance():
        if PersonSingleton.__instance is not None:
            PersonSingleton.__instance = None
            print("Singleton instance deleted")
            
            
PersonSingleton('Mike', 22)
PersonSingleton.print_data()

#PersonSingleton.delete_instance()
#PersonSingleton("David", 21)



