# Design-Patterns-in-Automation-Framework
## Types of design patterns:
1. Creational Patterns: <br/>
    Creational patterns are concerned with the process of object creation.
    Page Object:
      Page Object is a class that represents a web page and holds the web page elements and action methods. 
    Singleton Pattern: 
      ensures a class has only one instance and provides a global point of access to it.
    Factory Method Pattern: 
      Page Factory is a way to initialise the web elements we want to interact with within the page object when you create an instance of it. Defines an interface         for creating objects but lets subclasses decide which class to instantiate.
    Abstract Factory Pattern: 
      provides an interface for creating families of related or dependent objects without specifying their concrete classes.
    Builder Pattern: 
      separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
2. Structural Patterns: <br/>
    Structural patterns are concerned with object composition and the relationships between objects.
    Adapter Pattern: 
      adapts one class's interface to another interface that clients expect.
    Bridge Pattern: 
      decouples an abstraction from its implementation so that the two can vary independently.
    Composite Pattern: 
      composes objects into tree structures to represent part-whole hierarchies.
    Decorator Pattern: 
      attaches additional responsibilities to an object dynamically.
    Facade Pattern: 
      provides a unified interface to a set of interfaces in a subsystem.
3. Behavioral Patterns: <br/>
    Behavioral patterns are concerned with communication between objects, encapsulating behaviors in objects and manipulating them. 
    Observer Pattern: 
      defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    Command Pattern: 
      encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
    Interpreter Pattern: 
      defines a representation for a grammar of a given language, along with an interpreter that uses the representation to interpret sentences in the language.
    Iterator Pattern: 
      provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
    Template Method Pattern: 
      defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
