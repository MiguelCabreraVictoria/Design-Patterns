# Factory Method

### Intent

Is a creational desing pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created

### Solution 

- The factory method pattern suggest that you replace direct object construction call, with calls to a special factory method.

- Object returned by a factory method are often referred to as products

- At first glace, this change may look pointless: we just moved the constructor call from one part of the program to another. However, consider this: now you can override the factory method in a subclass and change the class of products being created in the method 

- Subclasses may return types of products only if these products have a common base class or interface

- The code that uses factory method doesn´t see a difference between the actual products returned by various subclasses.

- The client treats all the products as abstract interfaces and all these products are suppodes to have the interface´s method, but exactly how it works isn´t important to the client

### Structure

1. The product declares the interface, which is common to all objects that can be produced by the creator and its subclasses 

2. Concrete Product are different implementation of the product interface

3. The Creator class declasres the factory method that returns new products objects. It´s important that the return type of this method matches the product interface 

    - You can declare the factory method as abstract to force subclasses to implement their own versions of the method. As an alternative, the base factory metthod can return somo default product type

    - The product creation is not the primary responsibility of the creator. Usually the cretor class alredy has some core business logic related to products. The factory method helps to decouple this logic from the concrete product classes 

4. Concrete Cretor override the base factory method so it return a different type of product 

    - Note that the factory method doesn´t have to create new instances all the tme. It can also return existing objects form a cache, an object pool or another source

### Aplicability 

- Use the factory method when you don´t know beforehand the exact types of dependecies of the object your code should woork with

        - The factory method separates product construction code form the code that actually uses the product. Therefore it´s easier to extend the product construction code independently from the rest of the code

        - For example, to add a new product type to the app, you`ll only need to create a new creator subclass and override the factory method in it.

- Use the factory method when you want to provide users of your library or framework with a way to extend its internal components

- Use the factory method when you want to save system resources by reusing existing objects instead of rebuilding them each time

### How to implement

1. Make all prodcuts follow the same interface. This interface should declare methods that make sense in every product 

2. Add an empy factory method inside the creator class. The return type of the method should match the common product interface

3. In the creator´s code find all references to product constructors. One by one, replace them with a calls to the factory method, while extracting the product creation code into the factory method. You migth need to add a temporary parameter to the factory method to control the type of returned product. At his point, the code of the factory method may look pretty ugly. It may have a large switch statement that picks which product class to instantiate.

4. Create a set of creator subclasses for each type of product listed in the factory method. Override the factory method in the subclasses and extract the appropiate bits of construction code from the base mehthod.

5. If there are too many product types and it doesn´t make sense to create subclasses for all of them, you can reuse the control parameter form the base class in subclasses. For instance, imagine taht you hace following hierarchy of classes: the base Mail class with a couple of subclasses: AirMail and GroundMail; The Transport classes are Plane, Truck and Train. While the AirMail class only uses Plane objects, GroundMail mak work with both Truck and Train objects. You can create a new subclass (say TrainMail) to handle bothc cases, but there´s another option. The client code can pass an argyment to the factory method of the GroundMail class to control which product it wants to receive.

6. After all of the extractions, the base factory method has become empty, you can make it abstract. It there´s something left, you can make it default behavior of the method

### Pros

- You avoid tight coupling between the creator and the concrete products
- Single Responsability Principle: You can move the product creation code into one place in the program, making the code easier to support
- Open/Closed Principle: You can introduce new types of products into the program without breaking existing client code

### Cons

- The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you`re introducing the pattern into an existing hierarchy of creator classses
