# Overview
This is an overview of Good Code, Bad Code by Tom Long

# Goals of Code Quality 
- Code should work
- Code should keep working
- Code should be adaptable to changing requirements
- Code should not reinvent the wheel

# Pilars of Code Quality
- Make code readable
- Avoid suprises
- Make code hard to misuse
- Make code modular
- Make code reusable and generalizable
- Make code testable and test it properly

# Abstraction
- An important method for achiving four of the pillars of code quality: readability, modularity, reusability/generalizability, and testability
- Abstraction is the process of removing or hiding details to expose only the essential features of an object or concept
  - The visible (public) portion is the API (Application Programming Interface)
  - The hidden (private) portion is the implementation details
- What's an Interface?
    - An interface is a shared boundary across which two or more separate components of a computer system exchange information
    - In Java (and other languages) `Interface` is a formal keyword that defines a contract for a class to implement. For example, this interface, defines  getMeasure()
```java
public interface Measurable // <-- INTERFACE
{ 
    double getMeasure();
    // skipping implementaiton
}
public static double average(Measurable[] objects)
{
    double sum = 0;
    for (Measurable obj : objects)
    {
        sum = sum + obj.getMeasure();
    }
    if (objects.length > 0)
    {
        return sum / objects.length;
    }
    return 0;
}
```
This allows for different methods (`GetArea()` for Countries, `GetBallance()` for BankAccounts) to be averaged in the same way. So like a general interface it provides a (abstractio) boundary to implment a method across different classes.


- Interfaces need not be formal keywords. They also apply to classes and functions and describe the boundary and methods of exposing public information and hiding private information and is represented in the term Application Programming Interface (API)
    - Web APIs are where one usually first encounters the term. The Web API boundary is stark, it is well-defined. However APIs apply to Classes and functions as well. 
    - Take for example, the Pandas Library **API**: https://pandas.pydata.org/docs/reference/index.html

