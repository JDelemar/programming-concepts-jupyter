# Design Patterns

Design Patterns

## Types

- Types
  - **Creational patterns**: Focus on object creation mechanisms
    - **Factory Method** - Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. In other words, it delegates the responsibility of object creation to its subclasses, rather than creating objects directly within the superclass. Also known as virtual constructor.
    - **Abstract Factory** - Provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is similar to the Factory Method pattern in that it provides a way to encapsulate the creation of objects, but it is used when there are multiple types of related objects that need to be created.
    - **Builder**
    - **Prototype**
    - **Singleton**
  - **Structural patterns**: Deals with object composition and class relationships
    - **Adapter**
    - **Bridge**
    - **Composite**
    - **Decorator** - Allows you to dynamically add behaviors or responsibilities to objects without changing their original class structure. The pattern works by wrapping the original object with one or more decorator objects, each of which adds new behavior or functionality to the original object
    - **Facade**
    - **Flyweight**
    - **Proxy**
  - **Behavioral patterns**: Concentrate on communication between objects and classes
    - **Chain of Responsibility**
    - **Command**
    - **Iterator**
    - **Mediator**
    - **Memento**
    - **Observer** - Allows a one-to-many communication between objects so that when one object changes state (subject/observable), all its dependents are notified and updated automatically (observers/subscriber)
    - **State**
    - **Strategy** - Allows you to define a family of algorithms, encapsulate each one as an object, and make them interchangeable at runtime
    - **Template Method**
    - **Visitor**

## Defining Relationships

- Defining Relationships
  - Types of relations defined for classes under UML supported by mermaid

    Type | Description
    ---|---
    <|-- | Inheritance (IS-A) extends
    --> | Association (HAS-A)
    ..|> | Realization (implements) interface

### References

- References
  - [Refactoring Guru](https://refactoring.guru/)
  - [Mermaid class diagrams](https://mermaid.js.org/syntax/classDiagram.html)
  - Freeman, E., & Robson, E (2021). *Head First Design Patterns, 2nd Edition*. O'Reilly
