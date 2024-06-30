# Introduction

The Template Method design pattern is a behavioural design pattern that provides a way to define the skeleton of an algorithm in a base class, while allowing subclasses to customize or provide specific implementations for certain steps of the algorithm.

The pattern follows the principle of inversion of control, where the base class defines a template method that represents the overall algorithm. This template method consists of a series of steps or operations, some of which are common to all subclasses and some of which may vary.

# Real World Use

- Database Query Executions: In database query execution, there is a common structure for connecting to a database , executing a query , and retrieving the results. The template method pattern can be used to define a base class that provides  the overall structure
of the query execution algorithm, with subclasses customizing specific steps such as establishing a database connection, executing a query, and returning results.

- Report Generation: Generating different types of reports, such as financial reports or sales reports, often involves a common structure. The template method pattern can be utilized to define a base class that represents the overall report generation algorithm, with subclasses customizing specific steps such as gathering data, formatting the report, and generating output in different formats.

# Terminologies

- Abstract Class: Also known as the base class or the template class, it is an abstract class that defines the overall algorithm structure and provides a template method. The abstract class may contain both abstract and concrete methods.

- Concrete Class: These are the subclasses that inherit from the abstract class and provide concrete implementations for the abstract methods defined in the abstract class. Each concrete class represents a specific variation or customization of the algorithm.

- Template Method: This is a method defined in the abstract class, which provides the overall algorithm structure. It consists of a series of steps or method calls, some of which are implemented directly in the abstract class and others that are left to be implemented by the concrete subclasses.

# Notes

Template Method vs Strategy Pattern: The template method pattern and the strategy pattern share similarities, but they differ in theri intent. The template method pattern focuses on defining the overall algorithm structure with varying steps, while the strategy pattern
focuses on encapsulating interchangeable algorithms. The template method pattern uses inheritance, whereas the strategy pattern uses composition.