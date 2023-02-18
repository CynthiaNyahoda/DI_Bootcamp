# What is a class?
# A class is a blueprint or a template for creating objects. It defines the attributes and methods that an object will have, but does not create any objects itself.

# What is an instance?
# An instance is a specific object that is created from a class. It has all the attributes and methods that are defined in the class.

# What is encapsulation?
# Encapsulation is a principle of object-oriented programming (OOP) that refers to the practice of hiding the internal implementation details of an object from the outside world and only exposing a public interface. This allows for greater security, flexibility, and maintainability of code.

# What is abstraction?
# Abstraction is a principle of OOP that refers to the process of focusing only on the essential features of an object and ignoring its non-essential details. This helps to reduce complexity and improve efficiency in code design.

# What is inheritance?
# Inheritance is a mechanism in OOP that allows one class (the child or subclass) to inherit the attributes and methods of another class (the parent or superclass). This allows for code reuse and can help to simplify code structure.

# What is multiple inheritance?
# Multiple inheritance is a feature of some programming languages that allows a subclass to inherit from multiple parent classes. This can be useful in certain situations, but it can also lead to complexity and ambiguity in code design.

# What is polymorphism?
# Polymorphism is a principle of OOP that refers to the ability of objects of different classes to be used interchangeably. This is achieved through inheritance and method overriding, and allows for greater flexibility and code reusability.

# What is method resolution order or MRO?
# Method resolution order (MRO) is the order in which a programming language searches for methods to execute in a class hierarchy. It is used to determine which method to call when a method is inherited by multiple classes in a hierarchy. The MRO is often determined by a specific algorithm, such as C3 linearization in Python.



import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


