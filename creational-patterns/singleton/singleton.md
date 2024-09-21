# Singleton 

### Intent

Is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance

### Problem 

- Ensure that a class has just a single instance
        - Why would anyone want to control how many instances a class has? 
                - The most common reason for this is to control access to some shared resources
                - Instead of receiving a fresh object, you´ll get the one you already created, this behavior is impossible to implement with a regular constructor since a constructor call must always return a new object by design

- Provide a global access point to that instance
        - Just like a global variable, the Singleton pattern lets you access some sobject from anywhere in the program
        - However, it also protects that instance from being overwritten by other code

### Solution 

- Make the default constructor private, to prevent other objects from using new operator with the singleton class

- Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object 

### Structure

- The singleton class declares the static method 'getInstance' that returns the same instance of its own class

- The Singleton´s constructor should be hidden from the client code. Calling the 'getInstance' method should be the only way of getting the Singleton object

### Applicability 

- Use the singleton pattern when a class in your program should have a single instance available to all clients; for example, a single database object shared by different parts of the program 

    - The singleton pattern disables all other means of creating objects of a class except for the special creation method. This method either creates a new object or return an existing one if it has already been created


- Use the singleton pattern when you need stricter control over global variables

    - Inlike global variables, the Singleton pattern guarantees that there´s just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance

    - Note that you can always adjust this limitation and allow creating any number of Singleton instances. The only piece of code that needs changing is the body of the 'getInstance' method

### How to implement 

- Add a private static field to the class for storing the singleton instance

- Declare a public static creation method for getting the singleton instance

- Implement 'lazy initialization' inside the static method. It should create a new object on its first call and put it into the static field. The method should always return that instance on all subsequent calls

- Make the constructor of the class private. The static method of the class will still be able to call the constructor, but not the other objects 

- Go over the client code and replace all direct calls to the singleton´s constructor with calls to its static creation method

### Pros 

- You can be sure that a class only has only a single instance
- You gain a global access point to that instance
- The singleton object is initialized only when it´s requested for the first time

### Cons

- Violates the Single Responsibility Principle. The pattern solves two problems at the time
- The Singleton pattern can mask bad design, for instance, when the components of the program kwnow too much about each other
- The pattern requires special treatment in a multithreaded enviroment so that multiple threads won´t create a singleton object several times
- It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding static methods is impossibl in most languages, you will needd to think a creative way to mock the singleton.
