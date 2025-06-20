#list comprihension 
#List comprehension in Python is a concise way to create lists. It's a syntactic construct that allows you to generate a new list by performing an operation on each item in an existing iterable (like a list, tuple, or range). Essentially, it’s a shorthand for the more verbose for loop syntax.


#[expression for item in iterable]
#expression: The value or operation to add to the new list.
#item: The variable representing each element in the iterable.
#iterable: The collection of items you're iterating over (like a list or range).


#Example 1: Create a list of squares

squares = [x**2 for x in range(5)]
print(squares)


#output:

#[0, 1, 4, 9, 16]


#In this example, the expression is x**2, and the iterable is range(5).

#Example 2: Filter items based on a condition
#You can also include an if condition to filter items.


even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
#Output:


#[0, 2, 4, 6, 8]