# Programming Paradigms Coursework

## Overview

In this course, "Programming Paradigms," I will explore various major computer programming paradigms, such as imperative, functional, logic, and object-oriented programming. This course is designed to compare and contrast these different paradigms, offering me a comprehensive overview of diverse programming techniques. The course's key focus will be understanding and implementing alternative programming strategies within these paradigms.

I will be using Python and its libraries to apply these concepts practically. The course will emphasize writing well-documented code, breaking down complex code into manageable pieces, and mastering nested and cryptic coding techniques. A significant aspect of the course involves developing the ability to understand code written by others and crafting my own code in a clear and comprehensible way to other developers.

## Course Objectives

- Acquire a general understanding of different programming paradigms and related approaches.
- Assess how multiple programming paradigms relate to each other and impact program development experience.
- Choose better paradigms for specified problems.
- Write programs using a single paradigm.
- Write programs using multiple paradigms.
- Decide when particular programming paradigms will and will not be a proper choice for particular problems.

## Assignment 1 (Basic OOP)

#### Using objects:
1) Python provides us with many built-in objects. Here is some simple code where the first few lines should feel very simple and natural to you.

2) The first line constructs an object of type list, the second and third lines call the `append()` method, the fourth line calls the `sort()` method, and the fifth line retrieves the item at position 0. The sixth line calls the `__getitem__()` method in the stuff list with a parameter of zero. In this code, we call the `__getitem__` method in the list class and pass the list and the item we want retrieved from the list as parameters.

3) The last three lines of the program are equivalent, but it is more convenient to simply use the square bracket syntax to look up an item at a particular position in a list. We can take a look at the capabilities of an object by looking at the output of the `dir()` function:

#### Getting Started with OOP Programs:

4) At a basic level, an object is simply some code plus data structures that are smaller than a whole program. Defining a function allows us to store a bit of code and give it a name and then later invoke that code using the name of the function. An object can contain a number of functions (which we call methods) as well as data that is used by those functions. We call data items that are part of the object attributes. We use the class keyword to define the data and code that will make up each of the objects. The class keyword includes the name of the class and begins an indented block of code where we include the attributes (data) and methods (code).

5) As we have seen, in Python all variables have a type. We can use the built-in dir function to examine the capabilities of a variable. We can also use type and dir with the classes that we create.

#### Object lifecycle:

6) In the previous examples, we define a class (template), use that class to create an instance of that class (object), and then use the instance. When the program finishes, all of the variables are discarded. Usually, we don’t think much about the creation and destruction of variables, but often as our objects become more complex, we need to take some action within the object to set things up as the object is constructed and possibly clean things up as the object is discarded. If we want our object to be aware of these moments of construction and destruction, we add specially named methods to our object:

#### Multiple instances:

7) So far, we have defined a class, constructed a single object, used that object, and then thrown the object away. However, the real power in object-oriented programming happens when we construct multiple instances of our class. When we construct multiple objects from our class, we might want to set up different initial values for each of the objects. We can pass data to the constructors to give each object a different initial value:

8) Another powerful feature of object-oriented programming is the ability to create a new class by extending an existing class. When extending a class, we call the original class the parent class and the new class the child class.

## Assignment 2 (Abstract Factory Design Pattern)

1) First, we import the required modules for abstract classes and methods. `ABC (Abstract Base Class)` which helps in creating abstract classes which cannot be instantiated and typically contain one or more abstract methods. The second method is `abstractmethod` which is a decorator indicating abstract methods, which must be implemented by any subclass of the abstract class.

2) Define the abstract based class for the factory. `AbstractFactory` is an abstract class that declares methods for creating product. Products are chairs and their accessories in this context.

3) Define concrete factories. We implement concrete factories for creating specific product families. Our concrete factories are ModernChairFactory and VictorianChairFactory which inherit from AbstractFactory and implement the creation methods to return concrete products.

4) Next, we have to define our product interfaces. These are abstract classes for our products. AbstractChair and AbstractAccessory serve as base interfaces for chair and accessory products, respectively, declaring methods that concrete products must implement.

5) After that, we create concrete product classes for each product family. Concrete product classes (ModernChair, VictorianChair, ModernCushion, and VictorianCushion) implement the specific functionalities of the products, adhering to the interfaces defined by their abstract base classes.

6) We then implement our client code that works with factories and products through their abstract interfaces. The client_code function demonstrates how to interact with the products through the abstract factory and product interfaces. This allows changing product families without altering the client code.

7) Lastly, we test the implementation, executing the client code with different factories to test the abstract factory implementation. This block tests the abstract factory pattern by instantiating different concrete factories and passing them to the client_code function. It demonstrates the pattern's flexibility and how it enables the client code to use various product families interchangeably.  

## Assignment 3 (Builder Design Pattern)

1) First, we import the necessary Python libraries and modules that our example will rely on. This includes future annotations for forward reference of types, the ABC module for creating abstract base classes, and the abstractmethod decorator to define abstract methods within those classes. We also import Any from the typing module for type hinting.
   
2) Next, we define an abstract base `class (MealBuilder)` that specifies the blueprint for creating different parts of the meal. This class uses the `@abstractmethod` decorator to indicate that all subclasses must implement these methods.
   - `meal property`: A method to retrieve the meal object being built.
   - `prepare_starter`: Method to prepare the starter part of the meal.
   - `prepare_main_course`: Method to prepare the main course part of the meal.
   - `prepare_dessert`: Method to prepare the dessert part of the meal.

3) We then create a concrete `class (ItalianMealBuilder)` that implements the MealBuilder interface. This class is responsible for building a specific type of meal, in this case, an Italian meal, by providing concrete implementations of the building steps defined in the MealBuilder class.

4) After defining the builder, we need to create the product class (ItalianMeal) that the builder will construct. This class represents a complex object (a meal) that is being built part by part.

5) The `CulinaryDirector class` is responsible for executing the building steps in a specific sequence. This class is optional but useful for encapsulating and abstracting the construction process from the client.

6) Finally, we demonstrate how to use the Builder pattern in a client code scenario. This includes creating a director, setting a builder, and initiating the building process to create different types of meals.


## Assignment 4 (Singleton Design Pattern)

1) Create the Government class with the necessary attributes and methods.

2) Write the `__init__` method to initialize the object with the provided country, capital, and leader.

3) Define the `get_instance` class method to ensure only one instance of the Government class is created.

4) Add methods for displaying information, changing the leader, and getting GDP.

5) Demonstrate the usage of the Government class in the main function.


## Assignment 5 (Facade Design Pattern)

The primary goal of this assignment is to enhance the understanding and practical application of the Facade Design Pattern in simplifying complex systems. You are to provide with a basic implementation of an event management system that incorporates several subsystems: `VenueBooking`, `CateringService`, `PeopleCount`, and `NotificationSystem`. Your task is to refine this system, ensuring it offers a streamlined interface to its clients while maintaining the flexibility and functionality of the underlying subsystems.

## Assignment 6 (Proxy Design Pattern)

This assignment aims to deepen your understanding of the Proxy Design Pattern by extending a simple file access control system. You will provide a basic implementation that includes a `RealFileAccess` class performing actual file operations, and a `ProxyFileAccess` class controlling access to `RealFileAccess.` You are required to provide an enhanced system by implementing additional features and demonstrating the Proxy Pattern's effectiveness in access control and operation management.

## Assignment 7 (Chain of Responsibility)

In this assignment, you're tasked with developing a control system implemented in Python, which must utilize the Chain of Responsibility design pattern to grant access based on user roles ("basic" and "premium"). Your objective is to develop the system by adding at least two user roles (e.g., "guest" and "admin"), each with distinct access levels. This involves creating additional `ConcreteHandlers` for the new roles and integrating them into the  chain to maintain the pattern's decoupling principle. After implementation, you'll test the  system by processing orders with users of different roles, ensuring the system accurately grants or denies access. This assignment not only aims to deepen your understanding of the `Chain of Responsibility pattern but also enhances your ability to apply design patterns to real-world scenarios.
