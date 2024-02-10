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

Using objects:
1) Python provides us with many built-in objects. Here is some simple code where the first few lines should feel very simple and natural to you.

2) The first line constructs an object of type list, the second and third lines call the append() method, the fourth line calls the sort() method, and the fifth line retrieves the item at position 0. The sixth line calls the `__getitem__()` method in the stuff list with a parameter of zero. In this code, we call the `__getitem__` method in the list class and pass the list and the item we want retrieved from the list as parameters.

3) The last three lines of the program are equivalent, but it is more convenient to simply use the square bracket syntax to look up an item at a particular position in a list. We can take a look at the capabilities of an object by looking at the output of the `dir()` function:

Getting Started with OOP Programs:
4) At a basic level, an object is simply some code plus data structures that are smaller than a whole program. Defining a function allows us to store a bit of code and give it a name and then later invoke that code using the name of the function. An object can contain a number of functions (which we call methods) as well as data that is used by those functions. We call data items that are part of the object attributes. We use the class keyword to define the data and code that will make up each of the objects. The class keyword includes the name of the class and begins an indented block of code where we include the attributes (data) and methods (code).

5) As we have seen, in Python all variables have a type. We can use the built-in dir function to examine the capabilities of a variable. We can also use type and dir with the classes that we create.

Object lifecycle:
6) In the previous examples, we define a class (template), use that class to create an instance of that class (object), and then use the instance. When the program finishes, all of the variables are discarded. Usually, we don’t think much about the creation and destruction of variables, but often as our objects become more complex, we need to take some action within the object to set things up as the object is constructed and possibly clean things up as the object is discarded. If we want our object to be aware of these moments of construction and destruction, we add specially named methods to our object:

Multiple instances:
7) So far, we have defined a class, constructed a single object, used that object, and then thrown the object away. However, the real power in object-oriented programming happens when we construct multiple instances of our class. When we construct multiple objects from our class, we might want to set up different initial values for each of the objects. We can pass data to the constructors to give each object a different initial value:

8) Another powerful feature of object-oriented programming is the ability to create a new class by extending an existing class. When extending a class, we call the original class the parent class and the new class the child class.
