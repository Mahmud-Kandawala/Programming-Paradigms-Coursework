# Programming Paradigms Coursework

## Overview

In this course, "Programming Paradigms," we explore various major computer programming paradigms, including imperative, functional, logic, and object-oriented programming. This course is designed to compare and contrast these different paradigms, providing a comprehensive overview of diverse programming techniques. The focus is on understanding and implementing alternative programming strategies within these paradigms.

Python and its libraries are used to apply these concepts practically. The course emphasizes writing well-documented code, breaking down complex code into manageable pieces, and mastering nested and cryptic coding techniques. A significant aspect of the course involves developing the ability to understand code written by others and crafting clear and comprehensible code for other developers.

## Course Objectives

- Acquire a general understanding of different programming paradigms and related approaches.
- Assess how multiple programming paradigms relate to each other and impact program development experience.
- Choose the best paradigms for specific problems.
- Write programs using a single paradigm.
- Write programs using multiple paradigms.
- Decide when particular programming paradigms are appropriate or inappropriate for specific problems.

## Assignments

### Assignment 1: Basic OOP

#### Using Objects

1. Python provides many built-in objects. Below is simple code where the first few lines should feel familiar.
2. The first line constructs an object of type `list`, the second and third lines call the `append()` method, the fourth line calls the `sort()` method, and the fifth line retrieves the item at position 0. The sixth line calls the `__getitem__()` method in the `list` with a parameter of zero. Here, we use the `__getitem__` method to pass the list and the item we want retrieved from the list as parameters.
3. The last three lines of the program are equivalent, but it is more convenient to use square bracket syntax for item lookup in a list. We can examine an object's capabilities using the `dir()` function.

#### Getting Started with OOP Programs

4. At a basic level, an object is code plus data structures smaller than a whole program. Defining a function allows storing a bit of code, naming it, and invoking it later. An object can contain multiple functions (methods) and data used by those functions (attributes). We use the `class` keyword to define the data and code for each object.
5. In Python, all variables have a type. We can use `dir()` to examine a variable's capabilities and `type()` and `dir()` with the classes we create.

#### Object Lifecycle

6. We define a class (template), create an instance (object), use the instance, and discard variables when the program finishes. Sometimes, we need to take action within the object upon creation and destruction, adding specially named methods for these moments.

#### Multiple Instances

7. The real power in OOP is constructing multiple instances of a class, possibly setting different initial values for each object via constructors. Another powerful feature is creating a new class by extending an existing one (inheritance), where the original class is the parent, and the new class is the child.

### Assignment 2: Abstract Factory Design Pattern

1. Import the required modules for abstract classes and methods. Use `ABC` for creating abstract classes and `abstractmethod` for indicating abstract methods.
2. Define the abstract base class for the factory (`AbstractFactory`), declaring methods for creating products like chairs and their accessories.
3. Implement concrete factories (`ModernChairFactory` and `VictorianChairFactory`) inheriting from `AbstractFactory`, creating specific product families.
4. Define product interfaces (`AbstractChair` and `AbstractAccessory`) as abstract classes declaring methods for concrete products to implement.
5. Create concrete product classes (`ModernChair`, `VictorianChair`, `ModernCushion`, `VictorianCushion`) implementing the product interfaces.
6. Implement client code that interacts with factories and products through abstract interfaces, demonstrating the pattern's flexibility.
7. Test the implementation by executing client code with different factories, showcasing the abstract factory pattern's ability to handle various product families.

### Assignment 3: Builder Design Pattern

1. Import necessary Python libraries and modules (`future annotations`, `ABC`, `abstractmethod`, `Any`).
2. Define an abstract base class (`MealBuilder`) specifying the blueprint for creating meal parts.
3. Implement a concrete class (`ItalianMealBuilder`) providing specific implementations for building an Italian meal.
4. Create the product class (`ItalianMeal`) representing a complex object built part by part.
5. Implement the `CulinaryDirector` class to execute building steps in a specific sequence.
6. Demonstrate the Builder pattern in a client code scenario, creating a director, setting a builder, and building different meals.

### Assignment 4: Singleton Design Pattern

1. Create the `Government` class with necessary attributes and methods.
2. Write the `__init__` method to initialize the object with `country`, `capital`, and `leader`.
3. Define the `get_instance` class method to ensure only one instance of the `Government` class.
4. Add methods for displaying information, changing the leader, and getting GDP.
5. Demonstrate the `Government` class usage in the main function.

### Assignment 5: Facade Design Pattern

Enhance the understanding and practical application of the Facade Design Pattern by refining an event management system with subsystems (`VenueBooking`, `CateringService`, `PeopleCount`, `NotificationSystem`). Ensure the system offers a streamlined interface while maintaining subsystem flexibility and functionality.

### Assignment 6: Proxy Design Pattern

Extend a simple file access control system using the Proxy Design Pattern. Implement additional features in the `RealFileAccess` class performing file operations and the `ProxyFileAccess` class controlling access. Demonstrate the pattern's effectiveness in access control and operation management.

### Assignment 7: Chain of Responsibility

Develop a control system using the Chain of Responsibility design pattern to grant access based on user roles ("basic" and "premium"). Add roles (e.g., "guest", "admin") with distinct access levels, creating additional `ConcreteHandlers` and integrating them into the chain. Test the system by processing orders with different user roles, ensuring accurate access control.

---

Feel free to reach out for more information or if you have any questions regarding the Programming Paradigms Coursework.
